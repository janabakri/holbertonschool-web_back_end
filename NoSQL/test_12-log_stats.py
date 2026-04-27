#!/usr/bin/env python3
"""
Unit tests for 12-log_stats.py
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys

# استيراد السكريبت الأصلي
import lib_12-log_stats as log_stats


class TestLogStats(unittest.TestCase):
    """اختبار وظائف السكريبت"""

    @patch('lib_12-log_stats.MongoClient')
    def test_total_logs_count(self, mock_mongo_client):
        """اختبار عرض العدد الكلي للogs"""
        # تجهيز البيانات الوهمية
        mock_collection = MagicMock()
        mock_collection.count_documents.return_value = 1000
        mock_db = MagicMock()
        mock_db.nginx = mock_collection
        mock_client = MagicMock()
        mock_client.logs = mock_db
        mock_mongo_client.return_value = mock_client

        # اختبار الدالة
        with patch('sys.stdout', new=StringIO()) as fake_output:
            log_stats.log_stats()
            output = fake_output.getvalue()
            self.assertIn("1000 logs", output)

    @patch('lib_12-log_stats.MongoClient')
    def test_methods_output(self, mock_mongo_client):
        """اختبار عرض طرق HTTP بالترتيب الصحيح"""
        # تجهيز البيانات الوهمية للطرق المختلفة
        mock_collection = MagicMock()
        
        # ترتيب الاستدعاءات: GET, POST, PUT, PATCH, DELETE
        mock_collection.count_documents.side_effect = [500, 100, 50, 10, 5]
        
        mock_db = MagicMock()
        mock_db.nginx = mock_collection
        mock_client = MagicMock()
        mock_client.logs = mock_db
        mock_mongo_client.return_value = mock_client

        with patch('sys.stdout', new=StringIO()) as fake_output:
            log_stats.log_stats()
            output = fake_output.getvalue()
            
            # التحقق من وجود التبويب قبل كل طريقة
            self.assertIn("\tmethod GET: 500", output)
            self.assertIn("\tmethod POST: 100", output)
            self.assertIn("\tmethod PUT: 50", output)
            self.assertIn("\tmethod PATCH: 10", output)
            self.assertIn("\tmethod DELETE: 5", output)

    @patch('lib_12-log_stats.MongoClient')
    def test_status_check(self, mock_mongo_client):
        """اختبار حساب مسار /status"""
        mock_collection = MagicMock()
        
        # محاكاة استدعاء count_documents للـ status check
        def count_side_effect(query):
            if query.get("method") == "GET" and query.get("path") == "/status":
                return 250
            return 0
            
        mock_collection.count_documents.side_effect = count_side_effect
        
        mock_db = MagicMock()
        mock_db.nginx = mock_collection
        mock_client = MagicMock()
        mock_client.logs = mock_db
        mock_mongo_client.return_value = mock_client

        with patch('sys.stdout', new=StringIO()) as fake_output:
            log_stats.log_stats()
            output = fake_output.getvalue()
            self.assertIn("250 status check", output)

    @patch('lib_12-log_stats.MongoClient')
    def test_output_format(self, mock_mongo_client):
        """اختبار تنسيق المخرجات بالكامل"""
        mock_collection = MagicMock()
        mock_collection.count_documents.side_effect = [1000, 800, 100, 20, 10, 5, 400]
        
        mock_db = MagicMock()
        mock_db.nginx = mock_collection
        mock_client = MagicMock()
        mock_client.logs = mock_db
        mock_mongo_client.return_value = mock_client

        with patch('sys.stdout', new=StringIO()) as fake_output:
            log_stats.log_stats()
            output = fake_output.getvalue()
            lines = output.strip().split('\n')
            
            # يجب أن يكون 7 أسطر
            self.assertEqual(len(lines), 7)
            
            # السطر الأول: العدد + logs
            self.assertTrue(lines[0].endswith('logs'))
            
            # السطر الثاني: Methods:
            self.assertEqual(lines[1], "Methods:")
            
            # الأسطر 2-6: طرق HTTP مع تبويب
            for i in range(2, 7):
                self.assertTrue(lines[i].startswith('\t'))
                self.assertIn("method", lines[i])
            
            # السطر الأخير: status check
            self.assertIn("status check", lines[6])


if __name__ == '__main__':
    unittest.main()
