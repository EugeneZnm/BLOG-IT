import unittest
from app.models import Comments


class CommentsModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comments(comment='interesting article')

    # test instantiation of comment
    def test_instance(self):
        self.assertEqual(self.new_comment.comment, 'interesting article')

    # test comment saving
    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all()) > 0)

    # test getting comment by id
    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comment = Comments.get_comment(1)
        self.assertTrue(len(got_comment) > 0)
    
    # test comment deletion
    def test_delete_comment(self):
        self.new_comment.delete_comment()
        self.assertTrue(len(Comments.query.id()) > 0)
