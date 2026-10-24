import unittest
from analyze import load_data, scored_rows, metrics

class FraudAnalysisTests(unittest.TestCase):
    def test_sample_size_and_labels(self):
        con = load_data()
        result = metrics(scored_rows(con))
        self.assertEqual(result["transactions"], 20)
        self.assertEqual(result["chargebacks"], 6)
        con.close()

    def test_no_label_leakage(self):
        con = load_data()
        before = scored_rows(con)
        con.execute("UPDATE transactions SET chargeback = 1 - chargeback")
        after = scored_rows(con)
        self.assertEqual([(r[0], r[3]) for r in before],
                         [(r[0], r[3]) for r in after])
        con.close()

    def test_precision_bounds(self):
        con = load_data()
        m = metrics(scored_rows(con))
        self.assertGreaterEqual(m["precision"], 0)
        self.assertLessEqual(m["recall"], 1)
        con.close()

if __name__ == "__main__":
    unittest.main()
