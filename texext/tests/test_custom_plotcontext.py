""" Tests for plotcontext build using sphinx extensions

Test ability to combine plot_context with mathcode
"""

from os.path import dirname, join as pjoin

from sphinxtesters import ModifiedPageBuilder

from nose.tools import assert_equal, assert_regexp_matches

PAGES = pjoin(dirname(__file__), 'custom_plotcontext')


class TestPlotContext(ModifiedPageBuilder):
    # Test build and output of custom_plotcontext project
    page_source_template = PAGES

    def test_plot_and_math(self):
        doctree = self.get_doctree('plot_and_math')
        assert_equal(len(doctree.document), 1)
        tree_str = self.doctree2str(doctree)
        # Sphinx by 1.3 adds "highlight_args={}", Sphinx at 1.1.3 does not
        assert_regexp_matches(tree_str,
            '<title>Plot context with mathcode</title>\n'
            '<paragraph>Some text</paragraph>\n'
            r'<literal_block (highlight_args="{}"\s+)?language="python" '
            'linenos="False" xml:space="preserve">a = 101</literal_block>\n'
            '<only expr="html"/>\n'
            '<only expr="latex"/>\n'
            '<only expr="texinfo"/>\n'
            '<paragraph>More text</paragraph>\n'
            '<displaymath docname="plot_and_math" label="None" '
            'latex="101" nowrap="False"( number="None")?/>')
