import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Stack;
import java.util.Queue;

public class BST {
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }

    TreeNode root;

    TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        TreeNode current = root;
        while (true) {
            if (current.val < val) {
                if (current.right != null) {
                    current = current.right;
                } else {
                    current.right = new TreeNode(val);
                    break;
                }
            } else {
                if (current.left != null) {
                    current = current.left;
                } else {
                    current.left = new TreeNode(val);
                    break;
                }
            }
        }
        return root;
    }

    TreeNode searchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }
        if (root.val == val) {
            return root;
        }
        if (val < root.val) {
            return searchBST(root.left, val);
        } else {
            return searchBST(root.right, val);
        }
    }

    TreeNode getMin(TreeNode root) {
        TreeNode current = root;
        while (current.left != null) {
            current = current.left;
        }
        return current;
    }

    TreeNode deleteNode(TreeNode root, int val) {
        if (root == null) {
            return root;
        } else if (val < root.val) {
            root.left = deleteNode(root.left, val);
        } else if (val > root.val) {
            root.right = deleteNode(root.right, val);
        } else {
            if (root.left == null && root.right == null) {
                root = null;
            } else if (root.left == null) {
                root = root.right;
            } else if (root.right == null) {
                root = root.left;
            } else {
                TreeNode temp = getMin(root.right);
                root.val = temp.val;
                root.right = deleteNode(root.right, temp.val);
            }
        }
        return root;
    }

    List<Integer> inorderDFS(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;
        while (current != null || !stack.empty()) {
            while (current != null) {
                stack.add(current);
                current = current.left;
            }
            current = stack.pop();
            result.add(current.val);
            current = current.right;
        }
        return result;
    }

    List<Integer> preorderDFS(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) {
            return result;
        }
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;
        stack.add(current);
        while (!stack.empty()) {
            current = stack.pop();
            result.add(current.val);
            if (current.right != null) {
                stack.add(current.right);
            }
            if (current.left != null) {
                stack.add(current.left);
            }
        }
        return result;
    }

    List<Integer> postorderDFS(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) {
            return result;
        }
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;
        stack.add(current);
        while (!stack.empty()) {
            current = stack.pop();
            result.add(0, current.val);
            if (current.left != null) {
                stack.add(current.left);
            }
            if (current.right != null) {
                stack.add(current.right);
            }
        }
        return result;
    }

    List<List<Integer>> levelorderBFS(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> Q = new LinkedList<TreeNode>();
        Q.add(root);
        while (!Q.isEmpty()) {
            int size = Q.size();
            List<Integer> level = new ArrayList<Integer>();
            for (int i = 0; i < size; i++) {
                TreeNode current = Q.remove();
                level.add(current.val);
                if (current.left != null) {
                    Q.add(current.left);
                }
                if (current.right != null) {
                    Q.add(current.right);
                }
            }
            result.add(level);
        }
        return result;
    }

    int heightBST(TreeNode root) {
        if (root == null) {
            return -1;
        } else {
            int leftheight = heightBST(root.left);
            int rightheight = heightBST(root.right);
            if (leftheight > rightheight) {
                return leftheight + 1;
            } else {
                return rightheight + 1;
            }
        }
    }

    int getBalanceFactor(TreeNode root) {
        if (root == null) {
            return -1;
        } else {
            return (heightBST(root.left) - heightBST(root.right));
        }
    }

    TreeNode rightRotate(TreeNode root) {
        TreeNode x = root.left;
        // this is a right rotation meaning this is a left rotation
        // x will have second node after root : it will be root.left
        TreeNode y = x.right;
        // y will have x.right which in left rotation will be null (see diagram)
        x.right = root;
        // so the second node after root now becomes the root
        root.left = y;
        // the first node is still pointing to the second left node : just making it
        // null
        return x;
        // the root is moved down to the left of second node : this was left rotation
        /*
         * 30 (root)
         * /
         * 20 (x)
         * / \
         * 10 null
         * (y)
         * after right rotation :
         * 20 (x)
         * / \
         * 10 30
         * (root)
         */
    }

    TreeNode leftRotate(TreeNode root) {
        TreeNode x = root.right;
        // this is the left rotation meaning this is a right rotation
        // x will be the second node after root : it will be root.right
        TreeNode y = x.left;
        // y will have x.left which in right rotation will be null (see diagram)
        x.left = root;
        // so the second node after root becomes the root
        root.right = y;
        // the first node is still pointing to the second right node : just making it
        // null
        return x;
        // root is moved down to the right of the second node : this was right rotation
        /*
         * 10 (root)
         * \
         * 20 (x)
         * / \
         * null 30
         * (y)
         * after left rotation :
         * 20 (x)
         * / \
         * 10 30
         * (root)
         */
    }

    TreeNode insertAVL(TreeNode root, int val) {
        if (root == null) {
            root = new TreeNode(val);
            return root;
        }
        if (val < root.val) {
            root.left = insertAVL(root.left, val);
        } else if (val > root.val) {
            root.right = insertAVL(root.right, val);
        } else {
            // duplicate
            return root;
        }
        int balanceFactor = getBalanceFactor(root);
        // LL imbalance
        if (balanceFactor > 1 && val < root.left.val) {
            return rightRotate(root);
        }
        // RR rotation
        if (balanceFactor < -1 && val > root.right.val) {
            return leftRotate(root);
        }
        // LR rotation
        if (balanceFactor > 1 && val > root.left.val) {
            System.out.println("LR");
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }
        // RL rotation
        if (balanceFactor < -1 && val < root.right.val) {
            System.out.println("RL");
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }
        return root;
    }

    public static void main(String[] args) {
        BST tree = new BST();
        BST avlTREE = new BST();
        tree.root = tree.insertIntoBST(tree.root, 89);
        tree.root = tree.insertIntoBST(tree.root, -89);
        tree.root = tree.insertIntoBST(tree.root, 890);
        tree.root = tree.insertIntoBST(tree.root, -90);
        tree.root = tree.insertIntoBST(tree.root, -70);
        tree.root = tree.insertIntoBST(tree.root, 895);
        tree.root = tree.insertIntoBST(tree.root, 880);
        System.out.println(tree.inorderDFS(tree.deleteNode(tree.root, -89)));
        System.out.println(tree.inorderDFS(tree.root));
        System.out.println(tree.preorderDFS(tree.root));
        System.out.println(tree.postorderDFS(tree.root));
        System.out.println(tree.levelorderBFS(tree.root));
        System.out.println((tree.searchBST(tree.root, 880)).val);
        System.out.println(tree.heightBST(tree.root));
        System.out.println(tree.getBalanceFactor(tree.root));
        avlTREE.root = tree.insertAVL(avlTREE.root, 20);
        avlTREE.root = tree.insertAVL(avlTREE.root, 30);
        avlTREE.root = tree.insertAVL(avlTREE.root, 25);
        System.out.println(avlTREE.levelorderBFS(avlTREE.root));
        System.out.println(avlTREE.inorderDFS(avlTREE.root));
        System.out.println(avlTREE.preorderDFS(avlTREE.root));
        System.out.println(avlTREE.postorderDFS(avlTREE.root));
    }
}