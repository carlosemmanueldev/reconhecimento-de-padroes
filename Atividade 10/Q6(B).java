public class Q6(B) {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0310(b).png");
    int[][] result = new int[img.length][img[0].length];

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (img[i][j] < 107) {
          result[i][j] = 0;
        } else if (img[i][j] >= 107) {
          result[i][j] = 255;
        }
      }
    }

    ImagemDigital.plotarImagem(result, "Transformação linear");
  }
}