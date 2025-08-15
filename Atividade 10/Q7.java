public class Q7 {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0312(a).png");
    int[][] result1 = new int[img.length][img[0].length];
    int[][] result2 = new int[img.length][img[0].length];

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (150 <= img[i][j] && img[i][j] <= 255) {
          result1[i][j] = 153;
        } else {
          result1[i][j] = 25;
        }
      }
    }

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (150 <= img[i][j] && img[i][j] <= 200) {
          result2[i][j] = 204;
        } else {
          result2[i][j] = img[i][j];
        }
      }
    }
    
    ImagemDigital.plotarImagem(result1, "Resultado 1");
    ImagemDigital.plotarImagem(result2, "Resultado 2");
  }
}