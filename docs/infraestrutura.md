# Infraestrutura de publicação proposta

**Projeto:** Conserta Bairro  
**Autores:** Bernardo Haro Massignani e Marcelo Schuermann

## Escolha

Propomos usar **Cloudflare Pages** para os arquivos estáticos da PWA (HTML, CSS, JavaScript, manifesto e service worker) e **Supabase** para autenticação, API de dados e PostgreSQL. O navegador baixa o cliente pelo HTTPS do Pages e, quando precisa consultar ou alterar pedidos, conversa diretamente com a API do Supabase usando a sessão do usuário.

Essa divisão serve ao tamanho esperado do projeto: não precisamos administrar um servidor de aplicação só para disponibilizar os arquivos da interface. O Supabase reúne os serviços necessários para guardar pedidos e identificar usuários. A publicação do Pages pode acompanhar a branch `main` no GitHub. Para novas versões, planejamos revisar as mudanças, executar verificações automáticas e usar uma prévia antes de publicar.

## Por que essa opção

| Alternativa | Avaliação para este projeto |
| --- | --- |
| Cloudflare Pages + Supabase | Separa a hospedagem estática dos dados e evita manter servidor próprio. Atende ao PWA e ao cadastro de pedidos. São dois serviços para configurar. |
| Servidor próprio ou VPS | Dá mais controle, mas exige cuidar de sistema operacional, HTTPS, banco, backup e atualizações. Para a primeira versão do projeto, isso aumentaria o trabalho de operação. |
| Firebase Hosting + Firestore | Também atenderia ao caso, mas o grupo prefere modelar pedidos e seus relacionamentos (morador, voluntário e ponto de encontro) em PostgreSQL. |
| Apenas GitHub Pages | Publica a interface estática, mas não resolve sozinho autenticação e persistência dos pedidos. |

Não estamos afirmando que o sistema já está no ar. Esta entrega documenta a escolha de arquitetura. Para usar a nuvem posteriormente, ainda será necessário ativar as contas do grupo, criar o projeto Supabase, conectar o repositório ao Cloudflare Pages e configurar as variáveis públicas do cliente.

## Cuidados na implantação

- Habilitar Row Level Security (RLS) e conceder somente as operações necessárias em cada tabela exposta pela API.
- Exibir bairro e descrição do item na listagem; restringir dados de contato aos envolvidos no pedido.
- Guardar segredos administrativos fora do cliente e do repositório. A chave pública do cliente não substitui as políticas de acesso no banco.
- Servir o PWA por HTTPS, com manifesto e service worker. O cache ajuda na leitura sem conexão, mas atualizações de pedidos dependem da rede.
- Aplicar alterações do banco com migrações versionadas e verificar a aplicação antes de promover uma versão.

## Referências

- [Cloudflare Pages — integração com Git](https://developers.cloudflare.com/pages/get-started/git-integration/)
- [Supabase — plataforma](https://supabase.com/docs/guides/platform)
- [Supabase — segurança da API e RLS](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [MDN — requisitos de instalação de PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable)
