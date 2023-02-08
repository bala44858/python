import java.util.*;
 public class javaa{
    public static void main(String[] arg){
        Scanner obj = new Scanner(System.in);
        ArrayList<Integer> arr= new ArrayList<Integer>();
        HashMap<Integer, String> dic=new  HashMap<Integer,String>();
        int n=obj.nextInt();

        for(int i=0;i<n;i++){
           int a=obj.nextInt();
           dic.put(a," bala");
           arr.add(a); 
        }
        System.out.println(" first num "+arr.get(3));
        for (int j:arr){
            System.out.print(" " +j);
        }
        System.out.println();
        for (int j:dic.keySet()){
            System.out.print(dic.get(j));
        }


    }
}