from unittest import mock

from norma43utils.services.google_spreadsheet_service import GoogleSpreadsheetService


class TestService:
    @classmethod
    def setup_class(cls):
        cls.CONTENT = [
            [
                "20/02/2004",
                "20/02/2003",
                "0000000000001234567890123456",
                "COMPRA TARG 1234XXXXXXXX3456 SHOP TO BUY SEVERAL THINGS IN THERE.",
                "-23.99",
                "2439.44",
            ],
            [
                "20/02/2003",
                "20/02/2003",
                "AHSOWMSOWI8765SJWISU76WU",
                "INSURANCE COMPANY ABC DEF GHI JKL MNO PQRS TUVWXYZ                        ",
                "-70.29",
                "2369.15",
            ],
            [
                "20/02/2003",
                "20/02/2003",
                "A224E4ERF000000000123FFF",
                "INSURANCE COMPANY ABC DEF GHI JKL MNO PQRS TUVWXYZ                        ",
                "-70.29",
                "2298.86",
            ],
            [
                "20/02/2006",
                "20/02/2003",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .SUPERMARKET WHATEVER NAME INC.",
                "-138.57",
                "2160.29",
            ],
            [
                "20/02/2003",
                "20/02/2003",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .CAR GARAGE REPAIR.",
                "-1.00",
                "2159.29",
            ],
            ["20/02/2005", "20/02/2005", "FFF111FFF111FFF1", "SCHOOL OF ENGLISH ABC INC", "-96.00", "2063.29"],
            ["20/02/2005", "20/02/2005", "FFF111FFF111FFF1", "SCHOOL OF ENGLISH ABC INC", "-96.00", "1967.29"],
            ["20/02/2005", "20/02/2005", "000000000000                ", "PAYROLL", "500.00", "2467.29"],
            [
                "20/02/2010",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .CINEMA TICKETS.",
                "-43.25",
                "2424.04",
            ],
            [
                "20/02/2010",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .CARK PARK SERVICE",
                "-5.15",
                "2418.89",
            ],
            [
                "20/02/2011",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .CARK PARK SERVICE",
                "-4.65",
                "2414.24",
            ],
            [
                "20/02/2011",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .LIVE CONCERT",
                "-36.00",
                "2378.24",
            ],
            [
                "20/02/2011",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .RESTARUANT BON APETIT",
                "-19.31",
                "2358.93",
            ],
            [
                "20/02/2012",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 1234 .FAST FOOD RESTAURANT",
                "-26.70",
                "2332.23",
            ],
            ["20/02/2010", "20/02/2010", "ZZZWWDE53623609382735263", "LAWYERS SERVICE", "-24.20", "2308.03"],
            [
                "20/02/2013",
                "20/02/2010",
                "0000000000001234567890123456",
                "CREDIT CARD 1234567890123456 SUPERMARKET",
                "-6.44",
                "2301.59",
            ],
        ]

    @mock.patch(
        "norma43utils.services.google_spreadsheet_service.GoogleSpreadsheetService."
        "_retrieve_credentials_and_create_service"
    )
    @mock.patch("norma43utils.services.google_spreadsheet_service.GoogleSpreadsheetService.service")
    def test_write(self, m_service, m_retrieve_credentials_and_create_service):
        google_spreadsheet_service = GoogleSpreadsheetService()

        assert m_retrieve_credentials_and_create_service.call_count == 1

        google_spreadsheet_service.write(self.CONTENT, "spreadsheet_id")

        append = m_service.spreadsheets.return_value.values.return_value.append

        assert append.call_count == 1
        assert dict(**append.call_args.kwargs) == {
            "spreadsheetId": "spreadsheet_id",
            "range": "n43!A:F",
            "body": {
                "majorDimension": "ROWS",
                "values": [
                    [
                        "20/02/2004",
                        "20/02/2003",
                        "0000000000001234567890123456",
                        "COMPRA TARG 1234XXXXXXXX3456 SHOP TO BUY SEVERAL THINGS IN THERE.",
                        "-23.99",
                        "2439.44",
                    ],
                    [
                        "20/02/2003",
                        "20/02/2003",
                        "AHSOWMSOWI8765SJWISU76WU",
                        "INSURANCE COMPANY ABC DEF GHI JKL MNO PQRS TUVWXYZ                        ",
                        "-70.29",
                        "2369.15",
                    ],
                    [
                        "20/02/2003",
                        "20/02/2003",
                        "A224E4ERF000000000123FFF",
                        "INSURANCE COMPANY ABC DEF GHI JKL MNO PQRS TUVWXYZ                        ",
                        "-70.29",
                        "2298.86",
                    ],
                    [
                        "20/02/2006",
                        "20/02/2003",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .SUPERMARKET WHATEVER NAME INC.",
                        "-138.57",
                        "2160.29",
                    ],
                    [
                        "20/02/2003",
                        "20/02/2003",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .CAR GARAGE REPAIR.",
                        "-1.00",
                        "2159.29",
                    ],
                    ["20/02/2005", "20/02/2005", "FFF111FFF111FFF1", "SCHOOL OF ENGLISH ABC INC", "-96.00", "2063.29"],
                    ["20/02/2005", "20/02/2005", "FFF111FFF111FFF1", "SCHOOL OF ENGLISH ABC INC", "-96.00", "1967.29"],
                    ["20/02/2005", "20/02/2005", "000000000000                ", "PAYROLL", "500.00", "2467.29"],
                    [
                        "20/02/2010",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .CINEMA TICKETS.",
                        "-43.25",
                        "2424.04",
                    ],
                    [
                        "20/02/2010",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .CARK PARK SERVICE",
                        "-5.15",
                        "2418.89",
                    ],
                    [
                        "20/02/2011",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .CARK PARK SERVICE",
                        "-4.65",
                        "2414.24",
                    ],
                    [
                        "20/02/2011",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .LIVE CONCERT",
                        "-36.00",
                        "2378.24",
                    ],
                    [
                        "20/02/2011",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .RESTARUANT BON APETIT",
                        "-19.31",
                        "2358.93",
                    ],
                    [
                        "20/02/2012",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 1234 .FAST FOOD RESTAURANT",
                        "-26.70",
                        "2332.23",
                    ],
                    ["20/02/2010", "20/02/2010", "ZZZWWDE53623609382735263", "LAWYERS SERVICE", "-24.20", "2308.03"],
                    [
                        "20/02/2013",
                        "20/02/2010",
                        "0000000000001234567890123456",
                        "CREDIT CARD 1234567890123456 SUPERMARKET",
                        "-6.44",
                        "2301.59",
                    ],
                ],
            },
            "valueInputOption": "USER_ENTERED",
        }
