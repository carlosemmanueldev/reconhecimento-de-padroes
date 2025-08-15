public class Q6(A) {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0310(b).png");
    int[][] result = new int[img.length][img[0].length];

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (img[i][j] < 64) {
          result[i][j] = (int) (img[i][j] * 0.5);
        } else if (64 <= img[i][j] && img[i][j] <= 192) {
          result[i][j] = (int) (img[i][j] * 1.5 - 65);
        } else if (img[i][j] > 192) {
          result[i][j] = (int) (img[i][j] * 0.5 + 128);
        }
      }
    }

    ImagemDigital.plotarImagem(result, "Transformação linear");
  }
}