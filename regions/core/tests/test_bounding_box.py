# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from numpy.testing import assert_allclose
from astropy.tests.helper import pytest
from ..bounding_box import BoundingBox

try:
    import matplotlib

    HAS_MATPLOTLIB = True
except:
    HAS_MATPLOTLIB = False


def test_bounding_box_init():
    bbox = BoundingBox(1, 10, 2, 20)

    assert bbox.ixmin == 1
    assert bbox.ixmax == 10
    assert bbox.iymin == 2
    assert bbox.iymax == 20


def test_bounding_box_eq():
    bbox = BoundingBox(1, 10, 2, 20)
    assert bbox == bbox

    assert bbox != BoundingBox(99, 10, 2, 20)
    assert bbox != BoundingBox(1, 99, 2, 20)
    assert bbox != BoundingBox(1, 10, 99, 20)
    assert bbox != BoundingBox(1, 10, 2, 99)


def test_bounding_box_repr():
    bbox = BoundingBox(1, 10, 2, 20)

    assert repr(bbox) == 'BoundingBox(ixmin=1, ixmax=10, iymin=2, iymax=20)'
    assert eval(repr(bbox)) == bbox


def test_bounding_box_shape():
    bbox = BoundingBox(1, 10, 2, 20)

    assert bbox.shape == (18, 9)


def test_bounding_box_slices():
    bbox = BoundingBox(1, 10, 2, 20)

    assert bbox.slices == (slice(2, 20), slice(1, 10))


def test_bounding_box_extent():
    bbox = BoundingBox(1, 10, 2, 20)

    assert_allclose(bbox.extent, (0.5, 9.5, 1.5, 19.5))


@pytest.mark.skipif('not HAS_MATPLOTLIB')
def test_bounding_box_as_patch():
    bbox = BoundingBox(1, 10, 2, 20)

    patch = bbox.as_patch()
    assert_allclose(patch.get_xy(), (0.5, 1.5))
    assert_allclose(patch.get_width(), 9)
    assert_allclose(patch.get_height(), 18)