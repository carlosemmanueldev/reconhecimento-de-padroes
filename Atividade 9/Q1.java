class Q1 {
  public static void main(String[] args) {
    int[][] img1 = ImagemDigital.carregarImagem("lena_gray_512.png");
    int[][] img2 = ImagemDigital.carregarImagem("mandril_gray.png");
    float[] values = { 0.25F, 0.50F, 0.75F };

    for (int v = 0; v < 3; v++) {
      int[][] result = null;

      result = new int[img1.length][img1[0].length];
      for (int i = 0; i < img1.length; i++) {
        for (int j = 0; j < img1[i].length; j++) {
          result[i][j] = (int) (values[v] * img1[i][j] + (1 - values[v]) * img2[i][j]);
        }
      }

      ImagemDigital.plotarImagem(result, "Soma (" + values[v] + ")");
    }
  }
}