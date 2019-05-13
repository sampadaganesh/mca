class PQR
{
    int a, b;

    static void getdata()
    {
        a=10;
        b=20;
    }
}

class Sum extends PQR
{
    int sum;
 
    static void sum()
    {
        sum = a + b;
        System.out.print(" Sum = " + sum);
    }
}
 
class Subt extends Sum
{
    int subt;
 
   static void subtract()
    {
        subt = a - b;
        System.out.print(" Subtraction = " + subt + " ");
    }
}
 
class Abc
{
    public static void main(String args[])
    {
        Subt obj = new Subt();
        obj.getdata();
        obj.sum();
        obj.subtract();
    }
}