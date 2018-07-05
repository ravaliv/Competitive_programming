import java.util.*;
class LargestStack
{
	public Stack<Integer> s1 = new Stack<>();
	public Stack<Integer> s2 = new Stack<>();
	public void push(int item)
	{
		s1.push(item);
		if(s2.isEmpty() || item>=s2.peek())
		{
			s2.push(item);
		}
	}
	public int pop()
	{
		int item = s1.pop();
		if(item==s2.peek())
		{
			s2.pop();
		}
		return item;
	}
	public int getMax()
	{
		if(s2.isEmpty())
			return 0;
		return s2.peek();
	}
	public static void main(String[] args) {
		LargestStack l1 = new LargestStack();
		l1.push(5);
		System.out.println(l1.getMax());
        l1.push(4);
        l1.push(7);
        l1.push(7);
        l1.push(8);
        System.out.println(l1.getMax());
        System.out.println(l1.pop());
        System.out.println(l1.getMax());
        System.out.println(l1.pop());
        System.out.println(l1.getMax());
        System.out.println(l1.pop());
        System.out.println(l1.getMax());
        System.out.println(l1.pop());
        System.out.println(l1.getMax());

    
	}
}