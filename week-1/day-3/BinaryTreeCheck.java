public  class BinaryTreeCheck
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
    static Node root;
    static Node prev=null;
    public  static boolean isBST(Node node)
    {
    	if(node!=null)
    	{
    		if(!isBST(node.left))
    			return false;
    		if(prev!=null && node.value <= prev.value)
    			return false;
    		prev = node;
    		return isBST(node.right);
    	}
    	return true;
    }
    public static void main(String[] args) {
    	final Node n = new Node(50);
    	// final Node a = n.insertLeft(30);
    	 n.insertRight(70).insertRight(60).insertRight(80);
    	 // n.insertLeft(40).insertLeft(30).insertLeft(20).insertLeft(10);
    	// a.insertRight(60);
    	// a.insertLeft(20);
    	// final Node b = n.insertRight(80);
    	// b.insertLeft(70);
    	// b.insertRight(90);
    	final boolean result = isBST(n);
    	System.out.println(result);

    }
}