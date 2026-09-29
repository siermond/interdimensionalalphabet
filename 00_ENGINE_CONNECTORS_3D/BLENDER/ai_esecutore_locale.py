bl_info = {
    "name": "AI Esecutore Locale (Ollama)",
    "author": "Siermond Empire · Blender AI Bridge",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar (N) > AI Locale",
    "description": "Scrivi un comando in italiano e l'AI locale Ollama (qwen2.5-coder) lo esegue nella scena",
    "category": "3D View",
}

import bpy
import json
import urllib.request
import urllib.error
import re
import math
import mathutils

class AI_Props(bpy.types.PropertyGroup):
    prompt: bpy.props.StringProperty(
        name="Comando",
        description="Scrivi cosa vuoi creare o modificare nella scena",
        default="Crea una croce sacra in oro metallico e aggiungi un fascio di luce zenitale"
    )
    model: bpy.props.EnumProperty(
        name="Modello AI",
        description="Modello Ollama installato in locale da utilizzare",
        items=[
            ("qwen2.5-coder:7b", "Qwen 2.5 Coder 7B (Consigliato)", "Modello rapido e specializzato in codice Python per Blender"),
            ("qwen2.5-coder:14b", "Qwen 2.5 Coder 14B (Alta Precisione)", "Modello più grande per geometrie e animazioni complesse"),
            ("elevation:latest", "Elevation 7B", "Modello imperiale con spec di riserva ed elevazione"),
            ("rubin:latest", "Rubin 7B", "Modello Rubin Terminal locale"),
        ],
        default="qwen2.5-coder:7b"
    )
    last_code: bpy.props.StringProperty(
        name="Ultimo Codice",
        default=""
    )
    show_code: bpy.props.BoolProperty(
        name="Mostra Ultimo Codice Generato",
        default=False
    )

class WM_OT_ExecuteOllama(bpy.types.Operator):
    bl_idname = "wm.execute_ollama"
    bl_label = "Esegui Comando nella Scena"
    bl_description = "Invia la richiesta a Ollama ed esegue il codice Python generato"
    bl_options = {'REGISTER', 'UNDO'}

    prompt_override: bpy.props.StringProperty(name="Prompt Diretto", default="")

    def execute(self, context):
        props = context.scene.ai_props
        user_prompt = self.prompt_override if self.prompt_override else props.prompt
        model_name = props.model

        if not user_prompt.strip():
            self.report({'WARNING'}, "Scrivi prima un comando nella casella di testo!")
            return {'CANCELLED'}

        # 1. Raccoglie telemetria e contesto della scena per dare consapevolezza all'AI
        objs = [f"{o.name} ({o.type})" for o in bpy.data.objects][:25]
        active_obj = context.active_object.name if context.active_object else "Nessuno"
        selected_objs = [o.name for o in context.selected_objects]
        blender_ver = bpy.app.version_string

        system_prompt = (
            f"Sei un assistente esperto di programmazione Python per Blender {blender_ver} (modulo bpy). "
            f"Oggetti presenti nella scena: {', '.join(objs) if objs else 'Scena vuota'}. "
            f"Oggetto attivo selezionato: {active_obj}. "
            f"Oggetti attualmente selezionati: {', '.join(selected_objs) if selected_objs else 'Nessuno'}. "
            "Rispondi SOLO ed ESCLUSIVAMENTE con codice Python valido ed eseguibile con il modulo bpy. "
            "NON inserire commenti discorsivi, premesse, spiegazioni o testo fuori dai blocchi di codice. "
            "IMPORTANTE per Blender 4.x: per i materiali usa 'Principled BSDF'. "
            "Gli input del nodo Principled BSDF sono: 'Base Color', 'Metallic', 'Roughness', 'Emission Color', 'Emission Strength'. "
            "Accedi ai nodi con sicurezza. Il codice deve poter essere eseguito direttamente da exec()."
        )

        payload = {
            "model": model_name,
            "prompt": user_prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 1024
            }
        }

        url = "http://127.0.0.1:11434/api/generate"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )

        self.report({'INFO'}, f"Interrogo Ollama ({model_name})... attendi...")

        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                raw_reply = res_data.get("response", "")

            # Estrazione del codice Python pulito
            match = re.search(r"```(?:python)?\s*(.*?)```", raw_reply, re.DOTALL)
            clean_code = match.group(1).strip() if match else raw_reply.strip()

            # Rimozione di eventuali righe non-python in testa o coda
            lines = clean_code.splitlines()
            code_lines = [l for l in lines if not l.lower().startswith("ecco il codice") and not l.lower().startswith("here is")]
            clean_code = "\n".join(code_lines).strip()

            props.last_code = clean_code
            print("\n=======================================================")
            print(f"  [AI ESECUTORE] Codice generato da {model_name}:")
            print("=======================================================")
            print(clean_code)
            print("=======================================================\n")

            # Esecuzione del codice nella scena con Undo stack abilitato
            exec_globals = {
                "bpy": bpy,
                "math": math,
                "mathutils": mathutils,
                "context": context
            }
            exec(clean_code, exec_globals)

            self.report({'INFO'}, "✨ Comando eseguito con successo nella scena!")
            return {'FINISHED'}

        except urllib.error.URLError:
            self.report({'ERROR'}, "Impossibile connettersi a Ollama su 127.0.0.1:11434. Assicurati che Ollama sia avviato!")
            return {'CANCELLED'}
        except Exception as e:
            self.report({'ERROR'}, f"Errore esecuzione codice: {str(e)}")
            return {'CANCELLED'}


class WM_OT_ApplyQuickPreset(bpy.types.Operator):
    bl_idname = "wm.apply_quick_preset"
    bl_label = "Applica Preset"
    bl_description = "Invia un comando preimpostato rapido all'AI"

    preset_type: bpy.props.StringProperty(default="")

    def execute(self, context):
        props = context.scene.ai_props
        presets = {
            "FIRST_CROSS": "Crea una maestosa croce sacra al centro della scena, applica un materiale oro metallico lucido ed aggiungi un punto luce caldo che la illumini a 528 Hz.",
            "CYAN_CRYSTAL": "Crea una piattaforma circolare in pietra scura e posiziona sopra di essa un cristallo ottaedro ciano luminescente con bagliore emissivo.",
            "STUDIO_LIGHTS": "Aggiungi 3 luci di studio attorno all'oggetto al centro: una Key Light oro da destra, una Fill Light ciano da sinistra e una Rim Light bianca dall'alto.",
            "CLEAR_ALL": "Cancella tutti gli oggetti mesh presenti nella scena mantenendo la camera e le luci."
        }
        cmd = presets.get(self.preset_type, "")
        if cmd:
            props.prompt = cmd
            bpy.ops.wm.execute_ollama(prompt_override=cmd)
        return {'FINISHED'}


class VIEW3D_PT_OllamaPanel(bpy.types.Panel):
    bl_label = "AI Esecutore Locale (Ollama)"
    bl_idname = "VIEW3D_PT_ollama_executor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AI Locale'

    def draw(self, context):
        layout = self.layout
        props = context.scene.ai_props

        # Selettore modello Ollama
        box_model = layout.box()
        box_model.prop(props, "model")

        # Casella prompt utente
        box_cmd = layout.box()
        box_cmd.label(text="Cosa vuoi che accada nella scena?", icon='CONSOLE')
        box_cmd.prop(props, "prompt", text="")
        
        row_btn = box_cmd.row()
        row_btn.scale_y = 1.6
        row_btn.operator("wm.execute_ollama", text="⚡ ESEGUI COMANDO", icon='PLAY')

        # Comandi Rapidi (Preset Impero & Scena)
        layout.separator()
        box_presets = layout.box()
        box_presets.label(text="Comandi Rapidi:", icon='SOLO_ON')
        
        col_p = box_presets.column(align=True)
        op1 = col_p.operator("wm.apply_quick_preset", text="✝️ Crea Croce Sacra Oro First Cross", icon='COLORSET_01_VEC')
        op1.preset_type = "FIRST_CROSS"

        op2 = col_p.operator("wm.apply_quick_preset", text="💎 Cristallo Ciano Luminescente", icon='MATCUBE')
        op2.preset_type = "CYAN_CRYSTAL"

        op3 = col_p.operator("wm.apply_quick_preset", text="💡 Set 3 Luci Studio (Oro/Ciano)", icon='LIGHT')
        op3.preset_type = "STUDIO_LIGHTS"

        op4 = col_p.operator("wm.apply_quick_preset", text="🧹 Pulisci Scena (Cancella Mesh)", icon='TRASH')
        op4.preset_type = "CLEAR_ALL"

        # Ispettore ultimo codice generato
        layout.separator()
        row_toggle = layout.row()
        row_toggle.prop(props, "show_code", icon='TEXT')

        if props.show_code and props.last_code:
            box_code = layout.box()
            box_code.label(text="Ultimo Codice Python Eseguito:", icon='SCRIPT')
            for line in props.last_code.splitlines()[:15]:
                box_code.label(text=line)
            if len(props.last_code.splitlines()) > 15:
                box_code.label(text="... (apri la console di sistema per il codice completo)")


classes = (
    AI_Props,
    WM_OT_ExecuteOllama,
    WM_OT_ApplyQuickPreset,
    VIEW3D_PT_OllamaPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ai_props = bpy.props.PointerProperty(type=AI_Props)
    print("✨ [AI Esecutore Locale] Add-on registrato con successo in Blender! Trovalo nella Sidebar (N) > scheda 'AI Locale'.")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.ai_props

if __name__ == "__main__":
    register()
