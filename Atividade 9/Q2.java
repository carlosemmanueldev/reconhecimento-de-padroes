class Q2 {
  public static void main(String[] args) {
    int[][] img1 = ImagemDigital.carregarImagem("Fig0228(a).png");
    int[][] img2 = ImagemDigital.carregarImagem("Fig0228(b).png");

    subtraction(img1, img2);
    subtraction(img2, img1);
  }
  
  static void subtraction(int[][] img1, int[][] img2) {
    int[][] result = null;
    result = new int[img1.length][img1[0].length];
    
    for (int i = 0; i < img1.length; i++) {
      for (int j = 0; j < img1[i].length; j++) {
        result[i][j] = img1[i][j] - img2[i][j];
        
        if (result[i][j] < 0) {
          result[i][j] = 0;
        }
      }
    }
  
    ImagemDigital.plotarImagem(result, "Subtração");
  }
}