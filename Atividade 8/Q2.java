import java.util.ArrayList;

public class Q2 {
  public static void main(String args[]) {
    int[][] img1 = new int[300][300];
    int[][] img2 = new int[300][300];
    int[][] img3 = new int[300][300];

    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        if (j < 100 || j > 200 || i < 100 || i > 200) {
          img1[i][j] = 0;
          img2[i][j] = 64;
          img3[i][j] = 192;
        } else {
          img1[i][j] = 128;
          img2[i][j] = 128;
          img3[i][j] = 128;
        }
      }
    }

    ImagemDigital.plotarImagem(img1, "img1");
    ImagemDigital.plotarImagem(img2, "img2");
    ImagemDigital.plotarImagem(img3, "img3");
  }
}