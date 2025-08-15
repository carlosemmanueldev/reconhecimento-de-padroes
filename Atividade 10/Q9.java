import java.lang.Integer;

public class Main {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0314(a).png");
    int[][] bit7 = fatiar(img, 6);
    int[][] bit8 = fatiar(img, 7);

    int[][] result = new int[bit7.length][bit7[0].length];

    for (int i = 0; i < bit7.length; i++) {
      for (int j = 0; j < bit7[i].length; j++) {
        char binary1 = String.format("%8s", Integer.toBinaryString(bit7[i][j])).replaceAll(" ", "0").charAt(1);
        char binary2 = String.format("%8s", Integer.toBinaryString(bit8[i][j])).replaceAll(" ", "0").charAt(0);
        result[i][j] = (binary1 == '1' ? (int) Math.pow(2, 6) : 0) + (binary2 == '1' ? (int) Math.pow(2, 7) : 0);
      }
    }

    ImagemDigital.plotarImagem(result, "Questão 9");
  }

  static int[][] fatiar(int[][] img, int bit) {
    int[][] result = new int[img.length][img[0].length];

    for (int j = 0; j < img.length; j++) {
      for (int k = 0; k < img[j].length; k++) {
        result[j][k] = 255 * ((img[j][k] / (int) Math.pow(2, bit)) % 2);
      }
    }

    return result;
  }

}