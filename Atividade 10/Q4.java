import java.util.ArrayList;

public class Q4 {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0309(a).png");
    int[] gamas = { 3, 4, 5 };

    for (int k = 0; k < gamas.length; k++) {
      ArrayList<Integer> tonsDeCinza = tonsDeCinza(img);
      double c = Math.pow((tonsDeCinza.size() - 1), (1 - gamas[k]));

      int[][] newImg = new int[img.length][img[0].length];

      for (int i = 0; i < img.length; i++) {
        for (int j = 0; j < img[i].length; j++) {
          newImg[i][j] = (int) (c * Math.pow(img[i][j], gamas[k]));
        }
      }

      int max = max(newImg);
      int min = min(newImg);
      int[][] result = new int[newImg.length][newImg[0].length];
      for (int i = 0; i < newImg.length; i++) {
        for (int j = 0; j < newImg[i].length; j++) {
          result[i][j] = 255 * (newImg[i][j] - min) / (max - min);
        }
      }

      ImagemDigital.plotarImagem(result, "Transformação gama: " + gamas[k]);
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

  static int max(int[][] img) {
    ArrayList<Integer> tonsDeCinza = tonsDeCinza(img);
    int max = 0;

    for (int i = 0; i < tonsDeCinza.size(); i++) {
      if (tonsDeCinza.get(i) > max)
        max = tonsDeCinza.get(i);
    }

    return max;
  }

  static int min(int[][] img) {
    ArrayList<Integer> tonsDeCinza = tonsDeCinza(img);
    int min = 255;

    for (int i = 0; i < tonsDeCinza.size(); i++) {
      if (tonsDeCinza.get(i) < min)
        min = tonsDeCinza.get(i);
    }

    return min;
  }
}