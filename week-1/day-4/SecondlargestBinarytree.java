import java.util.*;
class SecondlargestBinarytree
{
	public static class Node
	{
		public int value;
        public Node left;
        public Node right;

        public Node(int value) 
        {
            this.value = value;
        }

        public Node insertLeft(int leftValue) 
        {
            this.left = new Node(leftValue);
            return this.left;
        }

        public Node insertRight(int rightValue) 
        {
            this.right = new Node(rightValue);
            return this.right;
        }
	}
	public static int findSecondLargest(Node rootNode)
	{
		if(rootNode == null || (rootNode.left == null && rootNode.right==null))
		{
			throw new IllegalArgumentException("A bst should contain a minimum of 2 nodes");

		} 
		Node current = rootNode;
		while(true)
		{
			if(current.left!=null && current.right==null)
			{
				return findLargest(current.left);
			}
			if(current.right !=null && current.right.left == null && current.right.right == null)
			{
				return current.value;
			}
			current=current.right;
		}
	}
	private static int findLargest(Node rootNode)
	{
		Node crnt = rootNode;
		while(crnt.right!=null)
		{
			crnt=crnt.right;
		}
		return crnt.value;
	}
	public static void main(String[] args) {
		Node n =new Node(50);
		n.insertRight(60).insertRight(70).insertRight(80);
        final int actual = findSecondLargest(n);
        System.out.println(actual);
	}
}