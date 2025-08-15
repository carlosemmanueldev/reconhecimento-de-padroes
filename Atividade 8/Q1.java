import java.util.ArrayList;

  public class Q1 {

  public static void main(String args[]) {
    int[][] img = ImagemDigital.carregarImagem("Fig0207.png");

    ArrayList<Integer> valores = new ArrayList<Integer>();
    for (int i = 0; i < img.length; i++) {
      for (int j = 0; j < img[i].length; j++) {
        if (!valores.contains(img[i][j])) {
          valores.add(img[i][j]);
          System.out.println(img[i][j]);
        }
      }
    }
  }
}