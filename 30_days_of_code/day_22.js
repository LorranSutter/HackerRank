

        // Add your code here
        if(root === null) return -1;

        let leftHeight = this.getHeight(root.left) + 1;
        let rightHeight = this.getHeight(root.right) + 1;

        return leftHeight > rightHeight ? leftHeight : rightHeight;
