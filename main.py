def twoSum(self,nums:List[int], target:int)->List[int]:
	c=[]
	for index_a,a in enumerate(List):
		for index_b,b in enumerate(List):
			if index_a==index_b:
				continue
			if a+b==targer:
				c.append(index_a)
				c.append(index_b)
				return c
			
