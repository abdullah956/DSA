import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class PascalTriangle{
    public static void main(String[] args) {
        List<List<Integer>> LLI = new ArrayList<>();
        Solution s = new Solution();
        System.out.println("enter the number of rows : ");
        Scanner sc = new Scanner(System.in);
        int numberofRows = sc.nextInt();
        LLI = s.generate(numberofRows);
        System.out.println(LLI);
        for(int i = 0; i<numberofRows; i++){
            System.out.println(LLI.get(i));
        }
        sc.close();
    }
}
class Solution{
    public List<List<Integer>> generate(int numberofRows){
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
        if(numberofRows == 0){
            return triangle;
        }
        List<Integer> firstRow = new ArrayList<Integer>();
        firstRow.add(1);
        triangle.add(firstRow); 
        for(int i = 1; i<numberofRows; i++){
            List<Integer> prevRow = new ArrayList<Integer>();
            prevRow = triangle.get(i-1); 
            List<Integer> row = new ArrayList<Integer>();
            row.add(1); 
            for(int j = 1; j<i; j++){
                row.add(prevRow.get(j-1)+prevRow.get(j));
            } 
            row.add(1);
            triangle.add(row);
        }
        return triangle;
    }
}