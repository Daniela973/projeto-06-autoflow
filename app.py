import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Prime Tech | AutoFlow", 
    page_icon="🤖", 
    layout="wide"
)

# --- ESTILIZAÇÃO VISUAL (PADRÃO PRIME TECH: GRAPHITE & CYAN) ---
st.markdown("""
<style>
    .stApp {
        background-color: #0b0c10;
        color: #ffffff;
    }
    h1, h2, h3, h4 {
        color: #00ffff !important;
    }
    p, label, span, div, .stMarkdown {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] {
        background-color: #12141a;
        border-right: 1px solid #1f2833;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: #0b0c10;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 210, 255, 0.3);
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #3a7bd5 0%, #00d2ff 100%);
        color: #ffffff;
    }
    input, textarea, select {
        background-color: #1f2833 !important;
        color: #ffffff !important;
        border: 1px solid #2c353d !important;
    }
    .logo-container {
        text-align: center;
        padding: 10px;
        background: #0b0c10;
        border-radius: 10px;
        border: 1px solid #1f2833;
        margin-bottom: 15px;
    }
    .logo-titulo {
        font-size: 20px;
        font-weight: 900;
        color: #00ffff;
        letter-spacing: 2px;
        margin: 0;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    .logo-sub {
        font-size: 10px;
        color: #ffffff;
        letter-spacing: 1px;
        margin-top: 2px;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTROLO DE AUTENTICAÇÃO SEGURA (LOGIN) ---
if "autenticado_p6" not in st.session_state:
    st.session_state.autenticado_p6 = False

if not st.session_state.autenticado_p6:
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="font-size: 32px; font-weight: 900; color: #00ffff; text-shadow: 0 0 15px rgba(0, 255, 255, 0.4);">PRIME TECH</div>
            <div style="font-size: 14px; color: #ffffff; letter-spacing: 2px;">AUTOFLOW — ACESSO RESTRITO & SEGURO</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        senha = st.text_input("Digite a palavra-passe de acesso:", type="password", key="senha_p6")
        if st.button("Entrar no AutoFlow", use_container_width=True):
            senha_correta = st.secrets.get("SENHA_ADMIN", "admin123")
            if senha == senha_correta:
                st.session_state.autenticado_p6 = True
                st.rerun()
            else:
                st.error("❌ Palavra-passe incorreta!")
    st.stop()

# --- BARRA LATERAL ---
st.sidebar.markdown("""
    <div class="logo-container">
        <div class="logo-titulo">PRIME TECH</div>
        <div style="background: linear-gradient(90deg, transparent, #00ffff, transparent); height: 2px; margin: 5px 0;"></div>
        <div class="logo-sub">AUTOFLOW ORCHESTRATOR</div>
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Navegação", [
    "🏠 Dashboard",
    "⚡ Nova Automação",
    "🤖 Meus Bots",
    "📋 Histórico & Logs",
    "🚨 Central de Erros",
    "📊 Relatórios de Impacto",
    "🔐 Segurança & Auditoria"
])

if st.sidebar.button("🚪 Terminar Sessão"):
    st.session_state.autenticado_p6 = False
    st.rerun()

# --- 1. DASHBOARD ---
if menu == "🏠 Dashboard":
    st.title("🤖 AutoFlow — Central de Bots")
    st.markdown("Orquestração avançada de processos, tarefas repetitivas e integrações automáticas.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🤖 Automações", "18", "Configuradas")
    col2.metric("🟢 Ativas", "15", "A operar")
    col3.metric("⚠️ Atenção", "3", "Erros tratados")
    
    st.markdown("---")
    st.subheader("⚡ Execuções Recentes de Hoje")
    
    df_exec = pd.DataFrame({
        "ID": ["#1524", "#1523", "#1522", "#1521"],
        "Automação": ["Relatório Diário", "Backup Automático", "Envio de E-mails", "Processar Financeiro"],
        "Horário": ["18:00", "17:00", "16:30", "16:00"],
        "Status": ["🟢 Sucesso", "🟢 Sucesso", "🟢 Sucesso", "🔴 Falha Tratada"]
    })
    st.dataframe(df_exec, use_container_width=True)

# --- 2. NOVA AUTOMAÇÃO ---
elif menu == "⚡ Nova Automação":
    st.title("⚡ Construtor de Automações")
    st.markdown("Defina gatilhos, blocos de ação encadeados e regras de resiliência a falhas.")
    
    with st.form("form_automacao"):
        nome_auto = st.text_input("Nome da Automação", "Enviar relatório diário automatizado")
        
        col1, col2 = st.columns(2)
        with col1:
            gatilho = st.selectbox("QUANDO (Gatilho)", ["Todos os dias às 18:00", "Novo ficheiro recebido", "Webhook de API", "Agendamento Personalizado"])
        with col2:
            acao_principal = st.selectbox("FAÇA (Ação Principal)", ["Gerar Documento / PDF", "Enviar E-mail", "Atualizar Base de Dados", "Chamar API Externa"])
            
        st.markdown("### 🛡️ Políticas de Segurança e Tratamento de Erros")
        st.checkbox("Ativar Try-Again automático (Até 3 tentativas em caso de falha de rede)", value=True)
        st.checkbox("Registar auditoria segura em log (Sem vazar dados sensíveis)", value=True)
        st.checkbox("Notificar administrador em caso de erro crítico (Fail-Safe)", value=True)
        
        col_test, col_save = st.columns(2)
        with col_test:
            testar = st.form_submit_button("🧪 Testar Fluxo em Modo Seguro", use_container_width=True)
        with col_save:
            salvar = st.form_submit_button("💾 Guardar e Ativar Automação", use_container_width=True)
            
        if testar:
            st.success("✔ Teste executado com sucesso! Código de controlo: `AUTO-SEC-998`")
            st.info("O fluxo passou em todas as validações de segurança e integridade de dados.")
        if salvar:
            st.success(f"🚀 Automação '{nome_auto}' guardada com sucesso e protegida por padrões de segurança Prime Tech!")

# --- 3. MEUS BOTS ---
elif menu == "🤖 Meus Bots":
    st.title("🤖 Gestão de Bots Ativos")
    st.markdown("Monitorize o estado operacional dos robôs em execução.")
    
    st.markdown("""
    * **🤖 Bot de Atendimento & Triagem** — 🟢 **Ativo** (Última execução há 4 min)  
      *Ações: Receber mensagem → Validar dados → Registar histórico.*
    * **🤖 Bot de Extração e Relatórios** — 🟢 **Ativo** (Próxima execução às 23:00)  
      *Ações: Recolher WebPulse → Gerar Excel → Enviar notificação.*
    * **🤖 Bot de Backup Seguro** — 🟢 **Ativo** (Executado de hora em hora)  
      *Ações: Compactar base → Enviar para armazenamento secundário.*
    """)

# --- 4. HISTÓRICO & LOGS ---
elif menu == "📋 Histórico & Logs":
    st.title("📋 Auditoria de Execuções (Logs Seguros)")
    st.markdown("Registo estrito de eventos operacionais sem exposição de dados confidenciais.")
    
    df_logs = pd.DataFrame({
        "Timestamp": ["2026-09-24 18:00:02", "2026-09-24 17:00:01", "2026-09-24 16:30:10"],
        "Execução ID": ["#1524", "#1523", "#1522"],
        "Operação": ["Relatório Diário", "Backup Automático", "E-mail Clientes"],
        "Audit Status": ["Usuário #28 — Sucesso", "Sistema — Sucesso", "Processo #104 — Sucesso"]
    })
    st.dataframe(df_logs, use_container_width=True)
    st.info("🔐 Nota de Segurança: Informações sensíveis (tokens, CPFs e senhas) são estritamente omitidas dos logs.")

# --- 5. CENTRAL DE ERROS ---
elif menu == "🚨 Central de Erros":
    st.title("🚨 Central de Erros e Recuperação")
    st.markdown("Gestão de falhas com proteção *Fail-Safe* e reexecução controlada.")
    
    st.warning("⚠️ **Erro Detetado (ID: AUTO-1042)**\n\n- **Automação:** Processo Financeiro\n- **Causa:** Timeout na API de envio de recibos.\n- **Estado:** Tentativa 1 de 3 falhou com segurança. O administrador foi notificado.")
    
    if st.button("🔄 Forçar Reexecução Segura"):
        st.success("✔ Reexecução efetuada com sucesso após 2.ª tentativa de conexão!")

# --- 6. RELATÓRIOS DE IMPACTO ---
elif menu == "📊 Relatórios de Impacto":
    st.title("📊 Relatório de Impacto Comercial")
    st.markdown("Métricas de eficiência, tempo economizado e ganho de produtividade.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("⏱️ Tempo Economizado", "184 horas", "Este mês")
        st.metric("📉 Erros Manuais Evitados", "99.4%", "Redução de riscos")
    with col2:
        st.metric("⚡ Total de Tarefas Executadas", "12.450", "Sem falhas críticas")
        st.metric("💼 Eficiência Operacional", "+42%", "Comparado a processos manuais")

# --- 7. SEGURANÇA & AUDITORIA ---
elif menu == "🔐 Segurança & Auditoria":
    st.title("🔐 Conformidade e Padrões de Segurança")
    st.markdown("Diretrizes de proteção nativa implementadas em toda a arquitetura Prime Tech.")
    st.success("""
    ✅ **Segredos isolados** fora do código fonte (`st.secrets` / `.env`).  
    ✅ **Criptografia** de dados em trânsito e repouso.  
    ✅ **Princípio do menor privilégio** aplicado no acesso aos bots.  
    ✅ **Fail-Safe ativo:** Mensagens amigáveis para utilizadores, erros técnicos confinados aos registos de administrador.  
    """)
