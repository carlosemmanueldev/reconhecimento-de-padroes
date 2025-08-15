import java.util.ArrayList;

public class Q1 {
  public static void main(String[] args) {
    int[][] img = ImagemDigital.carregarImagem("imagens/Fig0304(a).png");
    int[][] newImg = new int[img.length][img[0].length];

   ArrayList<Integer> tonsDeCinza = tonsDeCinza(img);

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        newImg[i][j] = tonsDeCinza.size() - 1 - img[i][j];
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

    ImagemDigital.plotarImagem(result, "Negativo da imagem Fig0304(a)(breast_digital_Xray)");
  }

   static ArrayList<Integer> tonsDeCinza(int[][] img) {
    ArrayList<Integer> tonsDeCinza = new ArrayList<Integer>();

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (!tonsDeCinza.contains(img[i][j])) tonsDeCinza.add(img[i][j]);
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