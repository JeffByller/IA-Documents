package codigo;
import java.util.Scanner;

public class SistemaBiblioteca {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Arrays para armazenar os livros
        String[] titulos = new String[100];
        String[] autores = new String[100];
        int totalLivros = 0;
        
        int opcao;
        
        do {
            // Menu do sistema
            System.out.println("\n=== SISTEMA BIBLIOTECA ===");
            System.out.println("1. Adicionar Novo Livro");
            System.out.println("2. Pesquisar Livro por Título");
            System.out.println("3. Excluir Livro pelo Título");
            System.out.println("4. Listar Todos os Livros");
            System.out.println("5. Sair do Sistema");
            System.out.print("Escolha uma opção: ");
            
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar o buffer
            
            switch (opcao) {
                case 1:
                    // Adicionar novo livro
                    if (totalLivros < titulos.length) {
                        System.out.print("Digite o título do livro: ");
                        String titulo = scanner.nextLine();
                        
                        System.out.print("Digite o autor do livro: ");
                        String autor = scanner.nextLine();
                        
                        // Validar campos obrigatórios
                        if (titulo.isEmpty() || autor.isEmpty()) {
                            System.out.println("Por favor, preencha todos os campos obrigatórios.");
                        } else {
                            titulos[totalLivros] = titulo;
                            autores[totalLivros] = autor;
                            totalLivros++;
                            System.out.println("Livro adicionado com sucesso!");
                        }
                    } else {
                        System.out.println("Biblioteca cheia! Não é possível adicionar mais livros.");
                    }
                    break;
                    
                case 2:
                    // Pesquisar livro por título
                    System.out.print("Digite o título para pesquisa: ");
                    String tituloPesquisa = scanner.nextLine();
                    
                    boolean encontrado = false;
                    for (int i = 0; i < totalLivros; i++) {
                        if (titulos[i].equalsIgnoreCase(tituloPesquisa)) {
                            System.out.println("Livro encontrado:");
                            System.out.println("Título: " + titulos[i]);
                            System.out.println("Autor: " + autores[i]);
                            encontrado = true;
                            break;
                        }
                    }
                    
                    if (!encontrado) {
                        System.out.println("Livro não encontrado.");
                    }
                    break;
                    
                case 3:
                    // Excluir livro pelo título
                    System.out.print("Digite o título do livro a ser excluído: ");
                    String tituloExcluir = scanner.nextLine();
                    
                    boolean excluido = false;
                    for (int i = 0; i < totalLivros; i++) {
                        if (titulos[i].equalsIgnoreCase(tituloExcluir)) {
                            // Remover o livro movendo os elementos
                            for (int j = i; j < totalLivros - 1; j++) {
                                titulos[j] = titulos[j + 1];
                                autores[j] = autores[j + 1];
                            }
                            totalLivros--;
                            System.out.println("Livro excluído com sucesso!");
                            excluido = true;
                            break;
                        }
                    }
                    
                    if (!excluido) {
                        System.out.println("Operação falhou: título não encontrado.");
                    }
                    break;
                    
                case 4:
                    // Listar todos os livros
                    if (totalLivros == 0) {
                        System.out.println("Nenhum livro cadastrado.");
                    } else {
                        System.out.println("\n=== LIVROS CADASTRADOS ===");
                        for (int i = 0; i < totalLivros; i++) {
                            System.out.println((i + 1) + ". Título: " + titulos[i] + " | Autor: " + autores[i]);
                        }
                        System.out.println("Total de livros: " + totalLivros);
                    }
                    break;
                    
                case 5:
                    System.out.println("Saindo do sistema...");
                    break;
                    
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
            
        } while (opcao != 5);
        
        scanner.close();
    }
}