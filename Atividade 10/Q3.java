import java.util.ArrayList;

public class Q3 {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0308(a).png");
    double[] gamas = { 0.6, 0.5, 0.4 };

    for (int k = 0; k < gamas.length; k++) {
      ArrayList<Integer> tonsDeCinza = tonsDeCinza(img);
      double c = (tonsDeCinza.size() - 1) / (Math.log(tonsDeCinza.size()) / Math.log(gamas[k]));

      int[][] result = new int[img.length][img[0].length];

      for (int i = 0; i < img.length; i++) {
        for (int j = 0; j < img[i].length; j++) {
          result[i][j] = (int) (c * (Math.log(1 + img[i][j]) / Math.log(gamas[k])));
        }
      }

      ImagemDigital.plotarImagem(result, "Transformação com log: " + gamas[k]);
    }
  }

  static ArrayList<Integer> tonsDeCinza(int[][] img) {
    ArrayList<Integer> tonsDeCinza = new ArrayList<Integer>();

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (!tonsDeCinza.contains(img[i][j]))
          tonsDeCinza.add(img[i][j]);
      }
    }

    return tonsDeCinza;
  }
}