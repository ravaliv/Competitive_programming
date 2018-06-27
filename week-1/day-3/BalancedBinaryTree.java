
public  class BalancedBinaryTree
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

	Node root;
	public static boolean isBalanced(Node node)
	{
		int lh;
		int rh;
		if(node == null)
			return true;
		lh = height(node.left);
		rh = height(node.right);
		if(Math.abs(lh-rh)<=1
			&& isBalanced(node.left)
			&& isBalanced(node.right))
			return true;
		return false;
	}
	public static int height(Node node)
	{
		if(node == null)
			return 0;
		return 1+Math.max(height(node.left),height(node.right));
	}
	public static void main(String[] args) {
		final Node root = new Node(1);
		// root.insertLeft(2).insertLeft(3);
		root.insertRight(4).insertRight(5).insertRight(6);
        // final Node a = root.insertLeft(8);
        // final Node b = root.insertRight(9);
        // b.insertLeft(8).insertLeft(7);
        // b.insertRight(5);
        // // a.insertLeft(1);
        // // a.insertRight(2);
        // b.insertLeft(3);
        // b.insertRight(4);
        final boolean result = isBalanced(root);
        System.out.println(result);

	}
}