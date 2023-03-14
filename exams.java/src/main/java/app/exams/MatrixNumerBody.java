package app.exams;

public class MatrixNumerBody {
  int[][] matrix;
  int num;

  public MatrixNumerBody() { }

  public MatrixNumerBody(int[][] matrix, int num) {
    super();
    this.matrix = matrix;
    this.num = num;
  }

  public int[][] getMatrix() {
    return this.matrix;
  }
  public void setMatrix(int[][] matrix) {
    this.matrix = matrix;
  }
  public int getNum() {
    return this.num;
  }
  public void setNum(int num) {
    this.num = num;
  }
}
