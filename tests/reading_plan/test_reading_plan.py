from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import Mock, patch
import pytest


def test_reading_plan_group_news():
    instance = ReadingPlanService()

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        instance.group_news_for_available_time(-2)

    mock_value = [
        {"title": "xablau e os xablau", "reading_time": 4},
        {"title": "xablau e xibliu", "reading_time": 5},
        {"title": "xablauzinho", "reading_time": 10},
        {"title": "xablauzao", "reading_time": 12},
    ]

    mock_find_news = Mock(return_value=mock_value)

    expected = {
        "readable": [
            {
                "unfilled_time": 1,
                "chosen_news": [
                    (
                        "xablau e os xablau",
                        4,
                    ),
                    (
                        "xablau e xibliu",
                        5,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "xablauzinho",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("xablauzao", 12),
        ],
    }

    with patch("tech_news.database.find_news", mock_find_news):
        result = instance.group_news_for_available_time(10)

    assert result == expected
