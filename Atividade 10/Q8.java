public class Q8 {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0314(a).png");
    int[] bits = { 0, 1, 2, 3, 4, 5, 6, 7 };

    for (int i = 0; i < bits.length; i++) {
      int[][] result = new int[img.length][img[0].length];

      for (int j = 0; j < img.length; j++) {
        for (int k = 0; k < img[j].length; k++) {
          result[j][k] = 255 * ((img[j][k] / (int) Math.pow(2, bits[i])) % 2);
        }
      }

      ImagemDigital.plotarImagem(result, (i + 1) + "º bit menos significativo");
    }
  }
}