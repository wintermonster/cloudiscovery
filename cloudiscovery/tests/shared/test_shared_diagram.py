from unittest import TestCase

from assertpy import assert_that

from shared.common import Resource, ResourceDigest
from shared.diagram import DiagramsNetDiagram
from shared.diagramsnet import MX_FILE

INFLATED_XML = "<xml />"
DEFLATED_XML = "s6nIzVHQtwMA"


class TestDiagramsNetDiagram(TestCase):
    sut = DiagramsNetDiagram()

    def test_deflate_encode(self):
        result = DiagramsNetDiagram.deflate_encode(INFLATED_XML)
        assert_that(result).is_equal_to(DEFLATED_XML)

    def test_decode_inflate(self):
        result = DiagramsNetDiagram.decode_inflate(DEFLATED_XML)
        assert_that(result).is_equal_to(INFLATED_XML)

    def test_file_generation(self):
        general_resources = [
            Resource(
                digest=ResourceDigest(id="123", type="type"),
                name="name",
                details="details",
            )
        ]
        grouped_resources = {"": general_resources}
        relations = []
        result = self.sut.build_diagram(grouped_resources, relations)
        assert_that(result).starts_with(MX_FILE[:200])
