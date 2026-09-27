# Conserta Bairro

Projeto de Práticas Extensionistas IV — Entrega 1  
Curso: Análise e Desenvolvimento de Sistemas — UNOESC

Professor: Jean Carlos Hennrichs

Bernardo Haro Massignani e Marcelo Schuermann

## Ideia

O Conserta Bairro é uma proposta de PWA para aproximar moradores que têm objetos domésticos com pequenos defeitos de voluntários e espaços comunitários que podem ajudar no conserto. A intenção é prolongar o uso dos objetos e facilitar o contato dentro do bairro.

O morador cadastra um pedido com categoria, descrição e bairro. Um voluntário pode aceitar o pedido e sugerir um ponto de encontro parceiro. O andamento fica registrado como aberto, combinado, concluído ou cancelado. Dados de contato e endereços pessoais não aparecem na listagem pública. Não há pagamento pelo aplicativo.

Nesta primeira entrega há **modelagem**, não uma aplicação publicada. Os diagramas mostram a arquitetura planejada para a implementação.

## Documentação da Entrega 1

- [PDF para entrega](output/pdf/Conserta_Bairro_Entrega_1.pdf)
- [Diagrama UML de pacotes](docs/diagrama-pacotes.pdf) ([versão editável em PlantUML](docs/diagrama-pacotes.puml))
- [Diagrama UML de implantação](docs/diagrama-implantacao.pdf) ([versão editável em PlantUML](docs/diagrama-implantacao.puml))
- [Diagrama de arquitetura DevOps](docs/diagrama-devops.pdf) ([versão editável em Mermaid](docs/diagrama-devops.mmd))
- [Decisão de infraestrutura](docs/infraestrutura.md)

## Recorte funcional

1. Cadastro e login de moradores e voluntários.
2. Abertura e consulta de pedidos por bairro e categoria.
3. Aceite do pedido por um voluntário.
4. Definição de um ponto de encontro parceiro e atualização de status.
5. Moderação de pedidos inadequados.

O PWA poderá guardar a interface e a última lista pública consultada para leitura sem conexão. Criar e atualizar pedidos exige conexão; assim evitamos mostrar como enviada uma operação que ainda não chegou ao servidor.

## Organização prevista

O cliente será uma PWA estática. A publicação do cliente está prevista no Cloudflare Pages, enquanto autenticação, API e PostgreSQL ficam em um projeto Supabase. A proposta detalhada e a comparação com outras opções estão em [infraestrutura.md](docs/infraestrutura.md). As contas e os recursos de nuvem ainda precisam ser criados antes da implementação.

## Referências consultadas

- Material de apoio de diagramas disponibilizado na disciplina.
- [Cloudflare Pages — integração com Git](https://developers.cloudflare.com/pages/get-started/git-integration/)
- [Supabase — visão geral da plataforma](https://supabase.com/docs/guides/platform)
- [Supabase — Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [MDN — instalação de PWAs](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable)
