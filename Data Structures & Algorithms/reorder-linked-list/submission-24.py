class Solution:

    def reorderList(self, head: Optional[ListNode]):
        self.cur = head

        def dfs(node):
            if not node:
                return True # Dùng flag để dừng

            if not dfs(node.next): # Nếu đã xử lý xong ở giữa thì dừng
                return False

            # Xử lý logic nối nút
            if self.cur.next == node or self.cur == node:
                node.next = None # QUAN TRỌNG: Ngắt đuôi để tránh loop
                return False # Dừng các bước đệ quy tiếp theo

            temp = self.cur.next
            self.cur.next = node
            node.next = temp
            self.cur = temp # Dịch chuyển cur lên
            return True
    
        dfs(head)
