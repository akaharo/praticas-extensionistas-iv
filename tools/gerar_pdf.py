"""Gera o PDF de entrega e as páginas individuais dos diagramas."""
from pathlib import Path
from math import atan2, cos, sin, pi

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "Conserta_Bairro_Entrega_1.pdf"
DOCS = ROOT / "docs"
OUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))

W, H = landscape(A4)
INK = colors.HexColor("#243247")
BLUE = colors.HexColor("#34628A")
LIGHT = colors.HexColor("#EEF3F7")
LINE = colors.HexColor("#9AACBA")
GREEN = colors.HexColor("#5A7D69")

c = canvas.Canvas(str(OUT), pagesize=(W, H))
c.setTitle("Conserta Bairro - Entrega 1 - Práticas Extensionistas IV")
c.setAuthor("Bernardo Haro Massignani; Marcelo Schuermann")
c.setCreator("Conserta Bairro")


def text(x, y, s, size=10, bold=False, color=INK):
    c.setFillColor(color)
    c.setFont("Arial-Bold" if bold else "Arial", size)
    c.drawString(x, y, s)


def lines(x, y, content, size=10, leading=15, bold=False, color=INK):
    for line in content:
        text(x, y, line, size, bold, color)
        y -= leading
    return y


def header(title, subtitle, page):
    c.setFillColor(BLUE)
    c.rect(0, H - 12, W, 12, fill=1, stroke=0)
    text(40, H - 50, title, 20, True)
    text(40, H - 69, subtitle, 9, False, BLUE)
    c.setStrokeColor(LINE)
    c.line(40, 43, W - 40, 43)
    text(40, 27, "Conserta Bairro | Práticas Extensionistas IV | Entrega 1", 8)
    text(W - 67, 27, str(page), 8, True)


def box(x, y, w, h, title, body, kind="plain", fill=LIGHT):
    c.setFillColor(fill)
    c.setStrokeColor(LINE)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    if kind == "package":
        c.setFillColor(fill)
        c.roundRect(x + 10, y + h - 1, min(w - 20, 105), 14, 2, fill=1, stroke=1)
    text(x + 13, y + h - 25, title, 11, True, BLUE)
    lines(x + 13, y + h - 44, body, 9, 14)


def arrow(x1, y1, x2, y2, label=None, dashed=False, label_dx=0, label_dy=8):
    c.setStrokeColor(BLUE)
    c.setFillColor(BLUE)
    c.setLineWidth(1.3)
    c.setDash(4, 3) if dashed else c.setDash()
    c.line(x1, y1, x2, y2)
    c.setDash()
    angle = atan2(y2 - y1, x2 - x1)
    # UML dependency: open arrow; deployment/process: filled arrow.
    head = 8
    for off in (pi / 6, -pi / 6):
        c.line(x2, y2, x2 - head * cos(angle + off), y2 - head * sin(angle + off))
    if label:
        mx, my = (x1 + x2) / 2 + label_dx, (y1 + y2) / 2 + label_dy
        text(mx - pdfmetrics.stringWidth(label, "Arial", 7) / 2, my, label, 7, False, INK)


# Página 1 - apresentação
header("Conserta Bairro", "Modelagem de um sistema de informação em formato PWA", 1)
text(42, 475, "Entrega 1 - Práticas Extensionistas IV", 14, True, BLUE)
text(42, 442, "Integrantes", 10, True)
lines(42, 423, ["Bernardo Haro Massignani", "Marcelo Schuermann"], 11, 19)
text(42, 360, "Repositório da disciplina", 10, True)
text(42, 340, "https://github.com/akaharo/praticas-extensionistas-iv", 10, False, BLUE)
c.linkURL("https://github.com/akaharo/praticas-extensionistas-iv", (42, 336, 330, 351), relative=0)
text(42, 290, "Proposta", 10, True)
lines(42, 271, [
    "O Conserta Bairro aproxima moradores que têm objetos domésticos com pequenos defeitos",
    "de voluntários e espaços comunitários que podem ajudar no reparo. O pedido informa",
    "categoria, descrição e bairro. Um voluntário aceita o pedido, combina um ponto de",
    "encontro e atualiza o andamento. O objetivo é facilitar o reaproveitamento no bairro.",
], 10, 16)
text(42, 176, "Escopo desta entrega", 10, True)
lines(42, 157, [
    "Este documento apresenta os três diagramas pedidos e a escolha da infraestrutura.",
    "A aplicação e os serviços em nuvem ainda não foram implantados; os fluxos mostram a",
    "arquitetura prevista para a etapa de desenvolvimento.",
], 10, 16)
c.showPage()


# Página 2 - UML de pacotes
header("1. Diagrama UML de pacotes", "Dependências entre as partes planejadas da aplicação", 2)
box(50, 345, 185, 100, "Interface PWA", ["Telas de pedidos", "Busca por bairro/categoria", "Formulários e estados"], "package")
box(50, 175, 185, 100, "Recursos PWA", ["Manifesto de instalação", "Service worker", "Cache de leitura"], "package")
box(325, 345, 185, 100, "Aplicação", ["Abrir e aceitar pedido", "Combinar encontro", "Atualizar e moderar"], "package")
box(325, 175, 185, 100, "Portas da aplicação", ["Interfaces de repositório", "Contrato de autenticação"], "package")
box(600, 345, 185, 100, "Domínio", ["Pedido e status", "Morador e voluntário", "Ponto de encontro"], "package")
box(600, 175, 185, 100, "Infraestrutura", ["Adaptadores Supabase", "Mapeamento de dados", "Cliente de autenticação"], "package")
arrow(235, 395, 325, 395, "usa", True)
arrow(142, 345, 142, 275, "usa recursos", True, 50, 0)
arrow(510, 395, 600, 395, "regras", True)
arrow(417, 345, 417, 275, "consulta/grava", True, 57, 0)
arrow(600, 225, 510, 225, "implementa", True)
arrow(692, 275, 692, 345, "mapeia", True, 38, 0)
text(50, 112, "Seta tracejada: o pacote na origem depende do pacote apontado.", 9)
text(50, 94, "O cache permite consultar dados já carregados; criar ou alterar pedidos depende de conexão.", 9)
c.showPage()


# Página 3 - UML de implantação
header("2. Diagrama UML de implantação", "Nós, ambientes de execução, artefatos e comunicação", 3)
box(48, 194, 245, 273, "<<device>> Dispositivo", ["Celular ou computador do usuário"], fill=colors.HexColor("#F8FAFC"))
box(67, 240, 207, 155, "<<executionEnvironment>>", ["Navegador", "", "<<artifact>> PWA", "Interface, manifesto, SW/cache"], fill=LIGHT)
box(365, 340, 225, 127, "<<node>> Cloudflare Pages", ["<<artifact>> arquivos estáticos", "HTML, CSS, JS, manifesto", "e service worker"], fill=LIGHT)
box(365, 134, 430, 157, "<<node>> Projeto Supabase", [], fill=colors.HexColor("#F8FAFC"))
box(382, 155, 173, 91, "<<executionEnvironment>>", ["Auth + Data API"], fill=LIGHT)
box(594, 155, 184, 91, "<<executionEnvironment>>", ["PostgreSQL", "Pedidos, usuários e", "pontos de encontro"], fill=LIGHT)
arrow(293, 400, 365, 400, "HTTPS · arquivos")
arrow(293, 284, 382, 201, "HTTPS · API + sessão", False, 1, 19)
arrow(555, 200, 594, 200, "SQL", False, 0, 10)
text(48, 98, "O cache ajuda a ler a lista pública sem conexão. Os pedidos atualizados ficam no Supabase.", 9)
text(48, 81, "RLS limita o acesso aos registros; dados de contato ficam restritos aos envolvidos no pedido.", 9)
c.showPage()


# Página 4 - DevOps
header("3. Arquitetura DevOps", "Fluxo planejado para quando a aplicação for desenvolvida", 4)
top_y, bot_y = 339, 175
ww, hh = 156, 93
xs = [48, 244, 440, 636]
box(xs[0], top_y, ww, hh, "Desenvolvimento", ["Código e modelagem", "na branch de trabalho"])
box(xs[1], top_y, ww, hh, "Pull request", ["GitHub", "Revisão pelo grupo"])
box(xs[2], top_y, ww, hh, "Verificações", ["GitHub Actions", "Lint, testes e build"])
box(xs[3], top_y, ww, hh, "Prévia", ["Cloudflare Pages", "Conferência antes do merge"])
box(xs[3], bot_y, ww, hh, "Branch main", ["Mudança aprovada", "e incorporada"])
box(xs[2], bot_y, ww, hh, "Publicação", ["Banco: migração, se houver", "Pages: PWA depois"])
box(xs[1], bot_y, ww, hh, "Verificação", ["Abrir PWA, testar fluxo", "e observar logs"])
box(xs[0], bot_y, ww, hh, "Resultado", ["Sem falha: versão disponível", "Falha: reverter/corrigir"])
for i in range(3):
    arrow(xs[i] + ww, top_y + 46, xs[i + 1], top_y + 46)
arrow(xs[3] + ww / 2, top_y, xs[3] + ww / 2, bot_y + hh, "aprovado", False, 46, 0)
for i in range(3, 0, -1):
    arrow(xs[i], bot_y + 46, xs[i - 1] + ww, bot_y + 46)
arrow(xs[0] + ww / 2, bot_y + hh, xs[0] + ww / 2, top_y, "se falhar", True, 37, 0)
text(48, 115, "Mudanças no banco são aplicadas antes do cliente que depende delas. Em caso de falha, o grupo corrige a versão.", 9)
text(48, 97, "Este é o processo proposto; ainda não há pipeline configurada ou aplicação publicada.", 9)
c.showPage()


# Página 5 - infraestrutura
header("4. Infraestrutura de publicação", "Escolha e justificativa para a primeira versão", 5)
text(42, 481, "Escolha: Cloudflare Pages + Supabase", 13, True, BLUE)
lines(42, 457, [
    "O Pages hospedará os arquivos estáticos da PWA em HTTPS. O Supabase oferecerá login, API e",
    "PostgreSQL para pedidos, usuários e pontos de encontro. A combinação evita manter um servidor",
    "próprio para um projeto pequeno e mantém os dados separados dos arquivos da interface.",
], 10, 16)
text(42, 392, "Alternativas consideradas", 10, True)
lines(42, 371, [
    "Servidor próprio/VPS: mais controle, porém exige configurar sistema, HTTPS, banco e backups.",
    "Firebase: atende ao caso, mas preferimos PostgreSQL para relacionar pedidos, pessoas e locais.",
    "Só GitHub Pages: hospeda a interface, mas não fornece sozinho login e persistência dos pedidos.",
], 9.5, 17)
text(42, 300, "Antes de publicar", 10, True)
lines(42, 279, [
    "Ativar as contas do grupo; criar o projeto Supabase; aplicar tabelas e políticas RLS; conectar",
    "o GitHub ao Cloudflare Pages; configurar variáveis públicas; testar a PWA e o fluxo de pedidos.",
    "Segredos administrativos não devem entrar no cliente nem no repositório. O service worker",
    "guardará a interface e a lista pública consultada. Envio e atualização exigirão conexão.",
], 9.5, 16)
text(42, 194, "Referências técnicas", 10, True)
lines(42, 176, [
    "Cloudflare Pages: developers.cloudflare.com/pages/get-started/git-integration/",
    "Supabase: supabase.com/docs/guides/platform e /database/postgres/row-level-security",
    "MDN PWA: developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable",
    "Material de Apoio Diagramas.pdf, disponibilizado na disciplina.",
], 8.2, 16)
c.showPage()
c.save()

reader = PdfReader(str(OUT))
for page_num, filename in [(1, "diagrama-pacotes.pdf"), (2, "diagrama-implantacao.pdf"), (3, "diagrama-devops.pdf")]:
    writer = PdfWriter()
    writer.add_page(reader.pages[page_num])
    with (DOCS / filename).open("wb") as f:
        writer.write(f)

print(OUT)
