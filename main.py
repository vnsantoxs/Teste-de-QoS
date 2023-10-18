import streamlit as st
import pandas as pd
import utils

if __name__ == '__main__':
    df_servidor = pd.read_excel(io="./TestesRede.xlsx",
                                sheet_name="Servidor",
                                usecols=["Interval", "Distance","Transfer", "Bandwidth", "Banda"])
    df_host = pd.read_excel(io="./TestesRede.xlsx",
                                sheet_name="Host",
                                usecols=["Interval", "Distance", "Transfer", "Bandwidth", "Banda"])
    st.title("TESTE DE QOS (Quality of Service)")
    st.divider()
    st.write("O objetivo deste teste de QoS (Quality of Service) é avaliar o desempenho de uma rede e de um serviço"
             "em termos de parâmetros como atraso, jitter, perda de pacotes, taxa de transferência, disponibilidade e"
             "confiabilidade. O teste de QoS aplicado foi realizado por meio da ferramentas Jperf que simula o "
             "tráfego e mede os indicadores de qualidade.")
    st.divider()
    st.subheader("COMPONENTES DO TESTE")
    col1, col2, col3 = st.columns(3)
    col1.subheader("Notebook Acer Aspire 3 AMD Ryzen 3")
    col1.write("- Wi-Fi 5")
    col1.write("- 802.11 ac/ax wireless")
    col1.write("- Dual band (2.4 GHz, 5 GHz)")
    col2.subheader("Notebook Ideapad Gaming 3i I5-11370h")
    col2.write("- Wi-Fi 5")
    col2.write("- 802.11 a/b/g/n/ac/ax wireless")
    col2.write("- MU - MIMO 2x2")
    col2.write("- Dual band (2.4 GHz, 5 GHz)")
    col3.subheader("Roteador Wireless DM986-414")
    col3.write("- 1000Mbps: - 200Mbps em 2.4GHz - 800Mbps em 5GHz")
    col3.write("- WAN Gigabit Ethernet")
    col3.write("- Dual band (2.4 GHz, 5 GHz)")
    col3.write("- NAT-Rotas Estáticas IPv4/IPv6")
    st.divider()
    st.subheader("CENÁRIO")
    st.write("A ferramenta jperf foi empregada para realizar os testes de qos do experimento, configurando o Notebook "
             "Ideapad Gaming 3i como host e o Notebook Acer Aspire 3 como servidor, ambos conectados ao Roteador "
             "Wireless DM986-414 que funcionava como concentrador. O jperf permitiu medir a largura de banda, "
             "o atraso, a perda de pacotes e o jitter da rede em diferentes distancias.")
    st.divider()
    st.subheader("TESTE 10 METROS")
    st.subheader("TESTE 20 METROS")
    st.subheader("TESTE 30 METROS")
    st.subheader("TESTE 40 METROS")
    st.subheader("TESTE 50 METROS")
    st.subheader("TESTE 75 METROS")
    st.subheader("CONCLUSÃO")



