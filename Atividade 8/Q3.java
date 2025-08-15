import java.math.*;

public class Q3 {

  public static void main(String args[]) {
    int[][][] img = ImagemDigital.carregarImagemCor("tove.jpg");
    int[][][] img1 = new int[500][500][3];
    int[][][] img2 = new int[500][500][3];
    int[][][] img3 = new int[500][500][3];
    int[][][] img4 = new int[500][500][3];
    int[][][] img5 = new int[500][500][3];

    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        img1[i][j][0] = img[i][j][0];
        img1[i][j][1] = img[i][j][1];
        img1[i][j][2] = Math.min(255, img[i][j][2] + 40);
        img2[i][j][0] = Math.min(255, img[i][j][0] + 40);
        img2[i][j][1] = Math.min(255, img[i][j][1] + 40);
        img2[i][j][2] = Math.min(255, img[i][j][2] + 40);
        img3[i][j][0] = Math.max(0, img[i][j][0] + (-40));
        img3[i][j][1] = Math.max(0, img[i][j][1] + (-40));
        img3[i][j][2] = Math.max(0, img[i][j][2] + (-40));
        img4[i][j][0] = Math.min(255, (int) (img[i][j][0] * 1.3));
        img4[i][j][1] = Math.min(255, (int) (img[i][j][1] * 1.3));
        img4[i][j][2] = Math.min(255, (int) (img[i][j][2] * 1.3));
        img5[i][j][0] = Math.min(255, (int) (img[i][j][0] * 0.7));
        img5[i][j][1] = Math.min(255, (int) (img[i][j][1] * 0.7));
        img5[i][j][2] = Math.min(255, (int) (img[i][j][2] * 0.7));
      }
    }

    ImagemDigital.plotarImagemCor(img, "tove");
    ImagemDigital.plotarImagemCor(img1, "img1");
    ImagemDigital.plotarImagemCor(img2, "img2");
    ImagemDigital.plotarImagemCor(img3, "img3");
    ImagemDigital.plotarImagemCor(img4, "img4");
    ImagemDigital.plotarImagemCor(img5, "img5");

  }
}
