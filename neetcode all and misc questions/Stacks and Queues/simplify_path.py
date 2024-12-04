'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: path = "/a/./b/../../c/"
Output: "/c"

Time complexity: O(N) (two passes total, one pass to remove all empty strings from list of directory elements, 
another pass to loop through our directory elements and operating on the stack)
space complexity: O(N) (since we're splitting by the parens, we need an additional list to hold our directory elements)

Approach:
Stack to keep track of our path so far, we append each directory, if we see a .. 
we can just pop off of the previous dir in our stack

empty stack = root directory

there's an added element of string parsing as well that we need to perform
so anything between two slashes is a directory, or either .. (previous dir) or . (stay on current dir)

split the string by '/' ? to get the content between the /
what do we do about '//'?

"/a/b/c/..//../d/".split('/') = ['', 'a', 'b', 'c', '..', '', '..', 'd', '']

remove all the empty strings in the list

path_list = ['a','b','c','..','..','d']

stack = []
['a', 'd']
build our path from the remaining stack, assuming we always have a / as the first character for the root
/a/d

Revisited on 12/4/2024 with a similar solution

'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = list(filter(lambda x: x != "", path.split("/")))
        stack = []
        for part in parts:
            if len(stack) > 0:
                if part == ".":
                    continue
                elif part == "..":
                    stack.pop()
                    continue
            # edge case if the first part is a .., this isn't valid since you can't go backwards
            # from the root directory, so we just ignore .., same with . as well, since the current directory
            # is just the root
            if part != ".." and part != ".":
                stack.append(part)
        # put the root directory slash back into the directory path, using the "/" as delimiter
        return "/" + "/".join(stack)

class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        s = "/a/./b/../../c/"
        "/" root
        "/a" from root, enter into dir a
        "/a/." dir a, same directory
        "/a/./b from a, enter into b
        /a/./b/.., from b, go back to previous directory (a)
        /a/./b/../.., from a, go back to previous directory (root)
        /a/./b/../../c/, from root, go into directory c
        evaluates to /c
        
        s = "/a/b/c/../../d/"
        "/" root
        "/a" from root, go to dir a
        "/a/b" from a, go to dir b
        "/a/b/c", from c, go into dir b
        "/a/b/c/..", from c, go back to previous dir (b)
        "/a/b/c/../../", from b, go back to previous dir (a)
        "/a/b/c/../../d", from a, go to dir d
        evaluates to "/a/d"
        
        '''
        split_slash = path.split('/')
        path_list = []
        for item in split_slash:
            if (item != ''):
                path_list.append(item)
        stack = []
        for i in range(len(path_list)):
            if (path_list[i] == '.'):
                continue
            elif (path_list[i] == '..'):
                if (len(stack) > 0):
                    stack.pop()
            else:
                stack.append(path_list[i])
        ## assume that the first slash represents root
        canonical_path = '/' + '/'.join(stack)
        return canonical_path

        