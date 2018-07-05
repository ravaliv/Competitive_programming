import java.util.*;
class Queuewith2stacks
{
	public Stack<Integer> s1 = new Stack<>();
	public Stack<Integer> s2 = new Stack<>();

	public void enQueue(int item)
	{
		s1.push(item);
	}
	public int dequeue()
	{
		if(s2.empty())
		{
			while(!s1.empty())
			{
				int item = s1.pop();
				s2.push(item);
			}
		

			if(s2.empty())
			{
				 throw new NoSuchElementException("Can't dequeue from empty queue!");

			}
		}
	
		return s2.pop();
	}
	public static void main(String[] args) 
	{
		Queuewith2stacks queue = new Queuewith2stacks();
		queue.enQueue(1);
		queue.enQueue(2);
		queue.enQueue(3);
        System.out.println( queue.dequeue());
        System.out.println( queue.dequeue());
        queue.enQueue(4);
        System.out.println( queue.dequeue());
        System.out.println( queue.dequeue());
    
	}


}