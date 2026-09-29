# Connettore Unreal Engine 5 ➔ Mirror Mountain & Interdimensional Alphabet

Questo modulo collega **Unreal Engine 5** con la regia cinematica di **Mirror Mountain** e **Interdimensional Alphabet**.

### Funzionalità:
1. **Remote Control Web Server (Porta 30010 HTTP)**:
   - Permette a Mirror Mountain e Nexus Command di inviare trigger remoti via REST/JSON.
2. **Ingestione Automatica GLB (Editor Python)**:
   - Importa direttamente `INTERDIMENSIONAL ALPHABET\01_ASHIA\ashia.glb` nel Content Browser (`/Game/InterdimensionalAlphabet/Ashia`).
3. **Regia Cinematica Sequencer**:
   - Coordina l'evento *Order Poem*:
     - Oscurità VR iniziale (Lumen / Raytracing disattivato/oscurato).
     - Discesa della Prima Croce Dorata con particle emitter Niagara.
     - Fascio di luce volumetrica zenitale.
     - Comparsa del Servant of Humanity con il Kybalion.
4. **Rendering Automatizzato**:
   - Supporto Movie Render Queue per formati verticali 9:16 (YouTube Shorts) e cinematica 16:9.

### Come attivare il Remote Control in Unreal Engine 5:
1. Apri il tuo progetto in Unreal Engine 5.
2. Vai in **Edit ➔ Plugins** e abilita:
   - *Remote Control API*
   - *Python Editor Script Plugin*
3. In **Project Settings ➔ Remote Control Web Server**, attiva l'avvio automatico del server (Porta predefinita: `30010`).
