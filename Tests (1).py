import unittest

import Shapes3D

SA = 'GetSurfaceArea'
Vo = 'GetVolume'

TEST_DATA = {
	Shapes3D.Cuboid: {
		SA: [
			([4.5910,2.1215,3.3676], 64.689643),
		],
		Vo: [
			([4.5910,2.1215,3.3676], 32.7997723694),
		],
	},
	Shapes3D.Cube: {
		SA: [
			([3.5312], 74.81624064),
		],
		Vo: [
			([3.5312], 44.031851491328),
		],
	},
	Shapes3D.Cylinder: {
		SA: [
			([4.9448,1.5906], 203.04896),
		],
		Vo: [
			([4.9448,1.5906], 122.1823),
		],
	},
	Shapes3D.Prism: {
		SA: [
			([1.5761,5,2.2727], 26.457657925613),
		],
		Vo: [
			([1.5761,5,2.2727], 9.7131170498483),
		],
	}
}

class TestShapeMethods(unittest.TestCase):

	def _testShape(self, shape:object, methods:dict, accuracy:int):

		for method, data in methods.items():

			for inputs, answer in data:
				result = getattr(shape(*inputs), method)()
				self.assertAlmostEqual(result, answer, accuracy)

	def test_shapes(self):
		for shape, methods in TEST_DATA.items():
			self._testShape(shape, methods, 4)

unittest.main()

