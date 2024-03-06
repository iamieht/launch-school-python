# Given a string s containing only '(', ')', '{', '}', '[' and ']', determine whether the string is valid. Valid means...
# opening brackets must be closed by the same type
# opening brackets must be closed in the proper order
# every closing bracket must have a corresponding opening bracket of the same type
# is_valid("{}")             -> True
# is_valid("[]{}()")         -> True
# is_valid("[)")             -> False
# is_valid("{{{}}})(")       -> False
# is_valid(")(")             -> False
# is_valid("[{]}[]{{}}")     -> True
