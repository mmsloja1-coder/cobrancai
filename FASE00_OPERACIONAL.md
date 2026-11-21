# COBRANÇAIA - FASE 00 COMPLETA: MANUAL OPERACIONAL

> **Princípio:** Você não vai vender IA. Você vai vender **DINHEIRO DE VOLTA SEM RISCO**.
> Landing → WhatsApp Business → Qualificação em 3 perguntas → Piloto de 14 dias → Relatório → Contrato.

---

## PARTE 0 - PRINCÍPIO QUE NÃO PODE FALHAR
- **Fase 00 NÃO é** vender para 100 empresas.
- **Fase 00 É** provar com 3 a 5 empresas que o Claude recupera dinheiro de verdade, com 1 processo repetível.
- **Meta:** 3 empresas piloto | 100 a 200 títulos por empresa | 14 dias | Recuperação > 8% = validação.
- **Regra de Ouro:** O Claude NUNCA envia sozinho. Ele **GERA**, você **REVISA** e **ENVIA**.

---

## PARTE 1 - ESTRUTURA DO PROJETO CLAUDE

Crie 1 Projeto no Claude chamado: **"CobrançaAI - Operação Fase 00"** com 3 arquivos.

### ARQUIVO 1 - INSTRUÇÕES DO PROJETO (Custom Instructions / System)

```
VOCÊ É O OPERADOR DA COBRANÇAAI - FASE 00
Seu trabalho é recuperar dinheiro de empresas, sem quebrar lei, sem queimar relacionamento e sem inventar dado.

REGRAS QUE NUNCA PODEM SER QUEBRADAS:
1. NUNCA invente valor, vencimento, multa, juros ou nome. Use SÓ o que está na planilha que eu enviar.
2. NUNCA use: "vou negativar", "vou processar", "seu nome vai sujar", "última chance", "URGENTE!!!", "protesto", "justiça", "advogado".
3. NUNCA mande mais de 1 mensagem a cada 48h para o mesmo cliente.
4. NUNCA mande fora de dias úteis, 8h às 19h.
5. SEMPRE comece com: "Oi [Nome], tudo bem? Aqui é [Seu Nome] da [Empresa Credora] via CobrançaAI."
6. SEMPRE ofereça 3 saídas: 1) Pix agora 2) Parcelar em 2x 3) Novo vencimento.
7. SE o cliente disser: "já paguei", "não devo", "me tira da lista", "não me chama mais", "vou processar": PARE. Não responda. Marque como [REVISÃO HUMANA URGENTE] e me avise.
8. SE o cliente pedir desconto maior que o permitido, NÃO conceda. Responda: "Vou confirmar com o financeiro da [Empresa] e te retorno."
9. LGPD: Nunca compartilhe dado de um cliente com outro. Nunca peça CPF, RG ou senha.
10. ANTES DE GERAR QUALQUER MENSAGEM, faça o CHECKLIST: Tem nome? Tem valor? Tem vencimento? Já foi cobrado nas últimas 48h? Está dentro do horário? Se 1 for NÃO, não gere.

FORMATO DE SAÍDA OBRIGATÓRIO - SEMPRE EM TABELA:
| Cliente | Valor | Dias de atraso | Mensagem pronta para copiar | Observação / Risco |

NUNCA envie a mensagem. Você GERA, eu REVISO e ENVIO.
Se eu te mandar uma resposta de cliente, você me devolve: 1) O que ele quis dizer 2) Resposta pronta seguindo as regras 3) Se devo parar ou continuar.
```

### ARQUIVO 2 - RÉGUA OFICIAL DE COBRANÇA

```
Use ESSA régua para todos os clientes. Sem exceção.

D-2 (2 dias antes do vencimento):
"Oi [Nome], tudo bem? Aqui é [Seu Nome] da [Empresa] via CobrançaAI. Passando pra lembrar que seu boleto de R$ [Valor] vence dia [Data]. Quer que eu já te mande o Pix pra facilitar?"

D0 (dia do vencimento):
"Oi [Nome], tudo bem? Hoje vence R$ [Valor] da [Empresa]. Te mando o Pix aqui pra você resolver rapidinho? Link: [Link]"

D+3 (3 dias depois):
"Oi [Nome], não identifiquei o pagamento de R$ [Valor] da [Empresa]. Aconteceu algo? Consigo te ajudar de 2 jeitos: parcelar em 2x ou gerar novo vencimento pra [Data]. O que fica melhor pra você?"

D+7:
"Oi [Nome], vi que ainda está em aberto R$ [Valor]. Pra não acumular, posso fazer assim: 1) Pix com novo vencimento 2) Parcelar em 2x. Qual você prefere? Se já pagou, me manda o comprovante que eu baixo na hora."

D+14 (encerramento do piloto):
"Oi [Nome], pra encerrar essa semana, me fala um dia que você consegue pagar que eu deixo agendado e não te chamo mais até lá. Pode ser dia [Data]?"

REGRA DE PAUSA: Se o cliente respondeu "vou pagar dia X", NÃO mande nada até X+1. Se ele pagou, PARE a régua na hora.
```

### ARQUIVO 3 - PLANILHA PADRÃO + REGRAS DO PILOTO

**Colunas obrigatórias:**
```
Nome | Telefone WhatsApp | Valor | Vencimento original | Nº Boleto / NF | Descrição | Desconto máximo permitido? | Parcelamento máximo? | Novo vencimento máximo?
```

**Regras definidas no Dia 0 com a empresa:**
- Desconto máximo: 0% ou 5% ou 10% (ela escolhe)
- Parcelamento máximo: 2x
- Novo vencimento: até 10 dias
- **Sem isso definido, o Claude NÃO opera.**

---

## PARTE 2 - WHATSAPP BUSINESS: SETUP COMPLETO

### Perfil
- **Nome:** CobrançaAI - Recuperação
- **Descrição:** "Recuperamos boletos e Pix em atraso para empresas. Piloto de 14 dias. R$ 0 fixo. 7% só sobre o que entrar de verdade."
- **Horário:** Seg a Sex, 8h às 19h
- **Catálogo:** 1 produto: "Piloto 14 dias - R$ 0 fixo, 7% só sobre recuperado"

### Mensagens Automáticas
**Saudação:**
> "Olá! Aqui é a CobrançaAI. 👋
> A gente recupera boletos e Pix em atraso para empresas, sem custo fixo. Você só paga 7% sobre o que entrar de verdade.
> Estamos com 3 vagas de piloto de 14 dias por mês.
> Quer que eu te explique como funciona o piloto?"

**Ausência:**
> "Oi! Recebemos sua mensagem. Respondemos em até 1 dia útil, das 8h às 19h. Se for sobre o piloto de 14 dias, já deixa aqui: qual sua empresa e quantos títulos em atraso você tem?"

### Respostas Rápidas (Salvar no WhatsApp Business)
| Atalho | Resposta |
|--------|----------|
| `/piloto` | Explicação completa do piloto (14 dias, 100 títulos, R$ 0 fixo, 7% sobre recuperado) |
| `/regras` | CDC/LGPD, 1 msg/48h, dias úteis, você define desconto/parcelamento |
| `/comecar` | "Perfeito! Preciso: 1) Nome da empresa e CNPJ 2) Responsável 3) Planilha com até 100 títulos" |

### Etiquetas de Organização
- `Novo lead` | `Aguardando planilha` | `Em piloto (Dia 1-14)` | `Aguardando pagamento 7%` | `Cliente fechado` | `Não respondeu`

---

## PARTE 3 - ABORDAGEM QUE CONVERTE

### Lista de Prospecção (20 empresas, não 100)
- 5 redes de escolas / cursos
- 5 clínicas / laboratórios / dentistas com rede
- 5 distribuidoras / fornecedores B2B
- 5 SaaS / software local / contabilidade com 100+ clientes

**NÃO aborda:** banco, telecom, hospital grande (jurídico de 6 meses).

### Script 1 - WhatsApp Frio (Mais Converte)
> "Oi [Nome], tudo bem? Sou [Seu Nome] da CobrançaAI.
> Vi que a [Empresa] trabalha com [mensalidade/boleto/contrato].
> A gente recupera boleto e Pix em atraso pra empresa de [segmento] cobrando só 7% sobre o que entrar. Sem mensalidade.
> Tô com 3 vagas de piloto de 14 dias com 100 títulos. Se não entrar nada, você não paga nada.
> Te mando o link com como funciona? [LINK DA LANDING]"

**Se responder SIM** → manda landing + `/piloto`
**Se responder "quanto custa?"** → `/piloto` + "É 7% só sobre o que entrar. Se recuperar R$ 10 mil, você paga R$ 700. Se recuperar 0, paga 0."
**Se não responder em 48h** → Follow-up 1.

### Script 2 - E-mail / LinkedIn
> **Assunto:** Piloto 14 dias - vocês só pagam se receberem
> 
> "Olá [Nome], vi que a [Empresa] atua com [segmento].
> Trabalho com recuperação de valores em atraso para empresas de [segmento]. Modelo: R$ 0 fixo, 7% só sobre o que for recuperado de verdade.
> Quero propor um piloto de 14 dias com 100 títulos, sem custo e sem compromisso. Se não recuperarmos nada, vocês não pagam nada.
> Link com como funciona: [LINK DA LANDING]
> Posso te mandar o modelo de 1 página com as regras do piloto?"

### Follow-up que Converte
- **Dia 3:** "Oi [Nome], só pra não perder: a vaga do piloto de [Mês] ainda está aberta. Quer que eu segure ela pra [Empresa] ou libero pra próxima da lista?"
- **Dia 6:** "Oi [Nome], entendo se não for o momento. Só te mando 1 exemplo: se a [Empresa] tem R$ 50 mil em atraso e a gente recuperar 10% em 14 dias, são R$ 5 mil de volta por R$ 350 de custo. Quer que eu te mostre como seria na sua base?"
- **Nunca mais que 2 follow-ups. No 3º, encerre:** "Vou liberar a vaga, se fizer sentido depois me chama."

### Qualificação no WhatsApp (3 Perguntas)
1. "Qual sua empresa e o que vocês vendem? Mensalidade, boleto, contrato?"
2. "Hoje, mais ou menos quanto você tem em atraso? Uma faixa já ajuda."
3. "Quem decide isso aí, é você mesmo?"

**Se responder bem:** "Fechado. Próximo passo: modelo de planilha + termo de piloto de 1 página. Mando agora?"
**Se enrolar:** "Sem problema. Quer que eu te mande a landing com o exemplo de relatório?"

---

## PARTE 4 - VALIDAÇÃO SEM FALHAS: CHECKLIST DIÁRIO

**Checklist do Operador (2 min por lote):**
- [ ] Planilha tem nome, telefone, valor, vencimento? (se faltar, não cobra)
- [ ] Cliente já foi cobrado nas últimas 48h? (se sim, pula)
- [ ] É dia útil, 8h às 19h? (se não, agenda)
- [ ] Desconto/parcelamento está dentro do que a empresa autorizou?
- [ ] Mensagem gerada pelo Claude foi lida por você? (nunca envia cego)
- [ ] Cliente pediu para parar? (se sim, marca como PARAR e nunca mais manda)
- [ ] Número é WhatsApp válido? (se não, marca como SEM CONTATO)

### Métricas de Validação (14 dias)
| Métrica | Meta | Ação se Falhar |
|---------|------|----------------|
| **Taxa de Resposta** | > 25% | Mensagem está fria → ajusta tom |
| **Taxa de Recuperação** | > 8% | Ajusta régua, não desiste |
| **Reclamações** | 0 | Obrigatório. Se >0, para tudo. |
| **Motivos** | Anotar: sem dinheiro / não reconhece / já pagou / vai pagar dia X | Ouro para próxima régua |

**Critério de Validação:** 2 de 3 empresas com > 8% recuperação e 0 reclamação = VALIDADO.

---

## PARTE 5 - PÓS-PILOTO: DO PILOTO AO CONTRATO

### Dia 0 - Onboarding
- Empresa manda planilha + assina termo de 1 página (WhatsApp com print).
- Define: desconto máximo, parcelamento máximo, novo vencimento máximo.
- Cria etiqueta "Em piloto" no WhatsApp Business.

### Dia 1 a 14 - Operação (40-60 min/dia/empresa)
| Horário | Ação |
|---------|------|
| **Manhã** | Cola planilha no Claude → "Quem devo cobrar hoje seguindo a régua?" → Claude gera tabela → Você revisa → Envia no WhatsApp |
| **Tarde** | Cliente respondeu? Cola no Claude → "O que respondo?" → Revisa → Envia. Pagou? Pede comprovante, confere extrato, marca PAGO, para régua. |

### Dia 14 - Relatório que Vira Contrato
```
RELATÓRIO PILOTO - [Empresa] - 14 dias
Títulos enviados: 100
Títulos cobrados: 92 (8 sem contato)
Responderam: 31 (33%)
Pagaram: 11 (12%)
Valor recuperado: R$ [X] com comprovantes anexos
Sua comissão 7%: R$ [Y]
Motivos de não pagamento: [lista]
Próximo passo: Quer continuar no mensal com a mesma regra?
```
*Anexe os comprovantes. Sem comprovante, sem cobrança de 7%.*

### Dia 15 - Conversão para Mensal
> "Fez sentido pra vocês? Para continuar, a gente mantém a mesma regra: R$ 0 fixo, 7% só sobre o que entrar, sem fidelidade. Você pode pausar quando quiser. Quer que eu já deixe a próxima leva de 100 títulos agendada?"

**Se SIM** → Primeiro cliente pagante. Pede depoimento: "O que mudou?"
**Se NÃO** → "O que precisaria mudar para fazer sentido?" → Ajusta para o próximo.

---

## PARTE 6 - CADÊNCIA PARA FECHAR O PRIMEIRO CLIENTE

| Período | Ação | Meta |
|---------|------|------|
| **Dia 1-2** | Lista 20 empresas + WhatsApp Business pronto + Landing no ar | Setup completo |
| **Dia 3-5** | 10 abordagens/dia (WhatsApp + LinkedIn) | 5 respostas |
| **Dia 6-7** | Follow-up + Qualificação | Fechar 1 piloto |
| **Dia 8-10** | Fecha 1 piloto → Opera bem → Depois fecha os outros 2 | 1 piloto ativo |

**Frase de Fechamento:**
> "Você é minha primeira empresa piloto do mês. Vou cuidar da sua carteira como se fosse a única, porque pra validar, eu preciso que a sua dê certo."

---

## RESUMO EM 1 LINHA (COLE NA PAREDE)
> **Landing → WhatsApp Business → 3 perguntas → Piloto 14 dias com 100 títulos → Claude gera, você revisa e envia → Relatório com comprovante → 7% só sobre o que entrou → Mensal.**

---

## PRÓXIMOS PASSOS IMEDIATOS
1. ✅ Landing Page atualizada e no ar
2. ✅ Repo GitHub: `https://github.com/mmsloja1-coder/cobrancai`
3. ✅ API Backend no ar: `https://cobrancai.onrender.com`
4. ⏳ **Próximo:** Configurar WhatsApp Business + Iniciar prospecção das 20 empresas
5. ⏳ **Meta:** Fechar 3 pilotos em 10 dias, operar 14 dias, fechar 3 mensais

---

*Documento salvo em: `/root/cobrancai/FASE00_OPERACIONAL.md`*
*Repo: `https://github.com/mmsloja1-coder/cobrancai`*