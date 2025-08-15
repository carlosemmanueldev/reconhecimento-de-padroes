import java.util.ArrayList;

public class Q5 {
  public static void main(String[] args) {
    int[][][] img = ImagemDigital.carregarImagemCor("imagens/a4d88a27b6e6f33558a8e675b742-1458995.jpg");
    double[] gamas = { 0.4, 2.7, 5.5 };

    for (int h = 0; h < gamas.length; h++) {
      ArrayList<Integer> tonsColoridos = tonsColoridos(img);
      double c = Math.pow((tonsColoridos.size() - 1), (1 - gamas[h]));

      int[][][] result = new int[img.length][img[0].length][3];

      for (int i = 0; i < img.length; i++) {
        for (int j = 0; j < img[i].length; j++) {
          for (int k = 0; k < img[i][j].length; k++) {
            result[i][j][k] = (int) Math.min(255, (c * Math.pow(img[i][j][k], gamas[h])));
          }
        }
      }

      ImagemDigital.plotarImagemCor(result, "Transformação gama: " + gamas[h]);
    }
  }

  static ArrayList<Integer> tonsColoridos(int[][][] img) {
    ArrayList<Integer> tonsColoridos = new ArrayList<Integer>();

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        for (int k = 0; k < img[i][j].length; k++) {
          if (!tonsColoridos.contains(img[i][j][k])) {
            tonsColoridos.add(img[i][j][k]);
          }
        }
      }
    }

    return tonsColoridos;
  }
}