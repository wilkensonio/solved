"""
20. Valid Parentheses
Easy
20.8K
1.3K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
	
	def isValid(self, s: str) -> bool:
		stack = []
		balanced = True
		index = 0
		while index < len(s) and balanced:
			symbol = s[index]
			if symbol in "([{":
				stack.append(symbol)
			else:
				if not stack:
					balanced = False
				else:
					top = stack.pop()
					if not Solution.matches(top, symbol):
						balanced = False
			index = index + 1
		
		return balanced and not stack
	
	def matches(open, close):
		opens = "([{"
		closers = ")]}"
		return opens.index(open) == closers.index(close)
