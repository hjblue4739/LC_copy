# Time:  ls: O(l + klogk), l is the path length, k is the number of entries in the last level directory
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)
# Space: O(n + s), n is the number of dir/file nodes, s is the total content size.

# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path,
#     return a list that only contains this file's name.
#     If it is a directory path, return the list of file and directory names in this directory.
#     Your output (file and directory names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist,
#       you should make a new directory according to the path.
#       If the middle directories in the path don't exist either,
#       you should create them as well. This function has void return type.
#
# addContentToFile: Given a file path and file content in string format.
#                   If the file doesn't exist, you need to create that file containing given content.
#                   If the file already exists, you need to append given content to original content.
#                   This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.
#
# Example:
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# Output:
# [null,[],null,null,["a"],"hello"]
#
# Note:
# 1. You can assume all file or directory paths are absolute paths
#   which begin with / and do not end with / except that the path is just "/".
# 2. You can assume that all operations will be passed valid parameters and
#   users will not attempt to retrieve file content or list a directory or file that does not exist.
# 3. You can assume that all directory names and file names only contain lower-case letters,
#   and same names won't exist in the same directory.


class TrieNode(object):

    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""

class FileSystem(object):

    def __init__(self):
        self.__root = TrieNode()


    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        curr = self.__getNode(path)

        if curr.is_file:
            return [self.__split(path, '/')[-1]]

        return sorted(curr.children.keys())


    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        curr = self.__putNode(path)
        curr.is_file = False


    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        curr = self.__putNode(filePath)
        curr.is_file = True
        curr.content += content


    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.__getNode(filePath).content


    def __getNode(self, path):
        curr = self.__root
        for s in self.__split(path, '/'):
            curr = curr.children[s]
        return curr


    def __putNode(self, path):
        curr = self.__root
        for s in self.__split(path, '/'):
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        return curr


    def __split(self, path, delim):
        if path == '/':
            return []
        return path.split('/')[1:]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)



'''
https://blog.csdn.net/magicbean2/article/details/78950619
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
Output:
[null,[],null,null,["a"],"hello"]
Explanation:

Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
————————————————
版权声明：本文为CSDN博主「魔豆Magicbean」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/magicbean2/article/details/78950619
思路：

文件系统构成了一个树状结构，所以本题目的一个解法就是建立一个树状结构来模拟文件系统。但是由于本题目是简化版的文件系统，所以我们也可以用更简单的字典树来实现。我们定义一个TrieNode的结构来统一表示文件和文件夹。如果isFile为true，则content表示文件的具体内容，此时children无效；否则children表示文件夹下的子文件（夹）列表，而content无效。下面给出各个函数的实现说明：

vector<string> ls(string path)：首先按照path给出的路径，在字典树中找到相应的文件（夹）。如果是文件，则返回它本身；否则就返回文件夹下面的所有子文件（夹）构成的列表。

void mkdir(string path)：按照path给出的路径，在字典树中找相应的文件夹，如果发现文件夹不存在，则新建文件夹。这样处理直到路径末尾。

void addContentToFile(string filePath, string content)：按照filePath给出的路径，在字典树中找相应的文件（如果文件或者文件夹不存在，则新建），最后将内容追加到找到（新建）的文件夹中即可。
————————————————
版权声明：本文为CSDN博主「魔豆Magicbean」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/magicbean2/article/details/78950619
'''


