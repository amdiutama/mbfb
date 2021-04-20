#Encrypt By Romi Afrizal (https://github.com/ROMI-AFRZL)

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJxFWMfO9Dpy/e69Mx7bS6/8AF4MoIVyAmzDiq3QSq2snXLOWVs/uN0/MGMTZJGgChRRLJ46xfTnb+VP3/Zf37aqX5F9628/3c9P9H/j336i3/4+/v0n+v0n//lp/vjJf/tp/vST//7T/Pkn+/3nv3/7W/2q/cn9Cvuvf3zXq//nW/T1X//l5ydXLtHXCoMUrh0ssNOpV7BiUz5WXymjGWfaLx2kKMjd9NC6OPAN9hv5JplGREZ5bO3L9RScH0TSyA6MAg9gBQ9/8Y/7DT4bDgL4XQAmuKMDWKMHvYMgZYPgZYEmABUm5R0mgHz74NvDRXG8iwIkl40E9YXeC7DLsQJEmxcB4gNAnfABAjAOFNaCChtMxJtUbLgrZXZwtXx1XOOlWrwauQhkO2LL+Dnc+hUG7vhmePs8LnPFh2ZqjHclhR8m9m/hDjBhzLjHl1artCNRtS3e4qSy2tWlWpV3mYo1VIhNFUt9o0ht3QcPDOh5z0ZNyfHPzKFgkcuKHVRnEXNkX+qM67BY47CQPchCGSBZU4RfWxowDYn6HE0TGJTlbIlntA/zPdznSbL+MIQeWuqs16yxD29DGtuD4DKZWwSlpbtWxWc2mULjHsWX4+ioDm8IRk+2hmkohZnnOVCs1KwP1nB6NR3BrAl0NUlTiUF4zy3WsbtRWbfGmTzhNc/4xznUgl/cXEtdaNiAfCQ+n9WqFf+Iy9BxA1xMIK7jdcKVj4Q3yilea/wdnRA9QLfvn53JbpRg5JMAwZ/veg8+nT3f01illaXIyouJH4JEYoYPXA9XIBmyuT52AZV5CvgBNOlSGBfRRzZs4SNIPjetjtqq159CQd4pjxeQvvKuMrR8ZAv03RjBkfSQJS6q/pLMpl6gyMDNr2mrqc2VfIXTWi+kEgegU5RYIIn6TrTsRpXxDjZPnhU6/wGf7NVQz9kfwtZUFPZIXLQ1YWiGE6Y8QnB4670lI1pnvapErICUz2aQWficvJPFH9h/INf094za8EboJ0Lvrn3gxLGTgelG+w/UKatzgseFO8qE8h3NWNXm92MX2IkMy6rn18otufAbERM2N2L9TfFZRgj9Or7KoTHXCgrE3axp0aAkvGaOK4FcYpIlD/4cJ+biX5uTt1u/cnc4i6x9tD7v1Zp9tbOJl/dYF7u1tj4FZVtfm9a7gS3anXqvlsS9QLqOWZ4wUEjGJa/Vvy7/NVY4AQelWCyfa8ioa+8nBZ/mXl5GI45atz3WKzS9xVNYOSp16yK/1r1iTQBTFJYstD/SoQ1AFxpFLiDwYF9HpuIXpQREDd19ZkQ6y5OycGvRBpRWhs8UClCJ3atF2sKS2gCosqHFxPrAGEpmkZsHjZd8HFsk2IatYTc3kgwqHL0mwoVDmyAxt61HJpOy90BXk81VJ7Vi6jSKCYi4a/j1sZCgp1BgTYS09UANImWNR3rZmaQ2H3wtjqSorZ6GvWunO28vxWcngLeq09800l3Y99w8xsc3BqVLvX4lHpejjxKXo2EToZ77CRs0GdLb1yuTgofSomdOuINc3bYQNjm2/ONFCsJWaCryIWvZhV65/nrcwSPR7xYiX0si7K7X3VBa+Z49+GC3OqFSr2oEjkvT+vbfX5Dl9vY9VJXiCWKSsA+mSDGBtmjLdGOcHlvXr/POtx35slyjr1ubSPNX4FY7R15bbw6VBWO0pRohSoUB6gT8dDGPMJ/Uk1JMjAJUsZl9k7Ft7fPaDb4EwLGLktbQ/hVg9M0HbJIQGg8GNMsNb58hJaXZ7VmGtC7QYBCux8fxCmsMz5X/bJmFvhkXmUnNPGz/g86ktYNoV9xvE6orPh+amRvG0n4Amkulj0+zUz7S/H430ESvBKdsrlbfd2g+vho/ue8CuXTZ2zxy6Dy9u42GOxmOHOjEyRjVSesUgHiijbBDUFCt9asR3rWn9EtSwzDT+2v8Is7RN3ujPCZfCiKdONhlyjXyXvDwuqRhQA1XOinjbsbcH6U77Afna2m24XbaqYKGzxOzXTS10ZGtTKnL8YtuEMzmNTgUWDBT0ef5HKPBxg/c9fgPfS6tNiOXlxm6KxdBfMi5L6qGCdj2cVvJs8vtWZIAOHvvTb/f7Na6TaYQnphKBwq6gqyi1lDyMJ1oKVqSlx+aY64VWz7jFZJ4L7Um81r2FGOlow8hCS3FEl5q0znKg5U52muiFwjCPTcrO9w7+VSsuwafMvIRBn3Q2ouCwoy/ruv7ZBnCMMXRmuWV5lRgTGOHvq6qV7nYslQatW6YHwPxdhW+CfFIMJsZAgx3Nij7LDaZZP3DEgZyqfcQVooq0aWqGaIgbW2YpCTz9rfyNZ/oG/EjxGU/jxIejxU5ch8LxC3iS7S2ONivYkRedEXgdRaXs1By4G2nK/dZaD8mbpeXrRXWuTZs1OUtMNZjc/s2LEtLjADwvTRa8HxIKIvNA61foZo3ZhgEh629y0p/dc7TARi7HlOxCex0vB5UpKTsLWtFpUZ5wj8s9wGAmG6CIh+C4t1J9cgFnTy4FDQrIhw97whAWPB67ZZwgdwNRK+ST+kThkd9KeG+ga9yPI+obpV+CvJXHQ0oso5wkFk5agb1KYWOVVMWMXXBGG6S4XSZp7oXv8swswiy+N0yocho5+LKo3j+ljX+2WZXJhwnwirv8Ul9eIk+3gxPSbHZS/E9KgSBMCQgjdBn+ESa1vuLN+HJvMYMWJHgYH0QVxRlhIaMAZtwEYRxlwWQlJWxgtabFqjuwFCzB3MO1Zchfr9n5K5BTMp1koBkG8XGZD6O9CNbyoIpsO4FMmtWW1NQpaEx3OcVq8TMBv4SR6P6YiQvLS2FQmhkqT06G5A2DXuYfN+zrtEpU3xMEhM95do/UKPFhGlNN0kCE+A5VXpl4zptAXWwkpgVxcbs+q3Ba6pKx4qjqzSTVwQshzsHKM3dXxdoadgjCC9CAOwG5ysXvS/WLiELADJjveOF0xWN0T2Pq3VsnefuwfwsgwIXtT5qfSiiio0F1Zs8H2lFhwysHmUC6nW8p9eb2LrefincJ3bseU+rNWlrSoYYr0/Bk6+/hAZAS7h9z5oj5wCt+AKtrwSVOp0WDcTX45rjZOHhxjAoZMrUZNjUIFEdBFdFOP1PgiLPjYQuq20Iiqvmx8Tl0ImH5o6uEpJpThSZ9/ROXaSk0xC07tZywODlsiBCwLIZlPBCyHVea98LNQJ8Fy8CQ9jn/KGRCzXNHI/NiPP7luXrMtlqtvT0kK+JMYF1vaKmeikBxiARA/MooAadMIDCIsglESLsBBBM2GQj5Dym0iKhS4dDjjDWPkDDEzyF0sGJlxWxr8xyQ6NR+sy5uaz36+pCZw3ISnIDC1DkFZWyqJAYb5w6aq/nvQsiDFYqRQPwNEv2Ab06jMDTCF7wxzRqsdbjX1IKIJ4O2HUW4EPyvLNI8Zg5QnMXf700TegW+MlYxqeIcdg52E8TjS7PpXalI4C4uyxx/qKNRA1h4htxOnWMiYYuIi172JQdKmjX6ePYN330u9G2CpcNbm0v06YDNwPWOvprb25n2Kha7Nn2+K9Duew5PMmAweeB2bs3BfEyR2vaosiGFAICcmgILCLYf1bdXNLoRTttNKmuswwu8bQuvGs8WbcqHBTJKeVjmLqNdJoSUKqz4gyHFqzlFfoTEgZGLL0RGIg8Khy1JI2PV7oojsx9kAqxylVMu1sSHCb+lDp+kay55Iwmz+h+0QStusKr1D6MRKhf1sgw0j5yxIejmW0Yt1gZvEapBrMDFLcbsJLn9sUKtdymyVSRSu3uQP7N2/xG24/83vOkTlDaHYYvIzTrlKKwHIRfg/3JaqqHajAXUu2Qdup4Eu+Dk6thBpZmO9nj6fG2aw45lSrHGeEKt1Llflkap34Wvhm8UyQv7mAb+Sk4svMth0nQCJBMJtoEhjluLumzBa42h6ytDcxQYXqe5/QrGu987/aqlSRXRD+OYMh55f358mZz3ht6jMJZL7W32SxA7upRumcgOgIhpiajnUKSjo9C+5itkts6vUoV7RuRaPILfMPa9nojGNFdstTgzEPZ0l4ylJxkUxKQJL0veC5ceAIakLyQLayK7fN+n24KlRAolr5K1PFmMFaZjpMiKOWt3yXpBQp33unNAVnFHShXCCNf9u7tKJ34gLCINu74eacY8MIhzz3NE0yt47D5brcqWYOE67sj6MqLZI8gMnldNicS2D7iDC6ZVPiyWnxaajnuHhSdvn8RybMchPLtQC0Ry9lmZVzzoZcivI9j8PRJxz/Jm7A0aOqZndh3h1csCnoNJVan5jSwY4LGvQDhWi6OcCtzKjuZeaLjzrpJfFiq3xzMfQ5UIAZURGk7DUXXruYBaNTKwoiD911aAhR622HF/HDgF3jg24Ykagk4Hz8J6kV2r+QhFUR6W60IFX12IcEXZ9f9Q146J8WGKe65FvhN15+mqDxD60roWn1TuM3SPKEwuXr8xBq5yV0i8iZ6rUQZecHZKJvXuzCYKiEEkRDGEfXJECekMLeylccrqHa4oLUvFcxxXy931LqZfCW+qXeyUAqQf9F1U8cZwECqKIlbCHm1KFuifN4aDW2BqurZeL2fGgcjwdZW4a09AbCMcK6enq2zJcd1Yz6/ys5xsDJI3+bhl6co+5SYXeM+N6qwikbNmq1AoC6dk70gu/BTvdMS/VgU56gQf7h4/CTkl4YxyTNPjFrbzOu+v6k47az8842AKCfU25vSBpaxWFYkH9zSChAoKdB8wMRESbHlrmUonGQ5SRV6ioneN6Wfz693wiAQLXRnOAtdAyBST6Jeoo87Pwu9Al/C2qwwhOeg6QUMkIBXsZBvmp4BIj+AI6vuI/8GUgoEFxJMSJB+Yyx7Qdp//PUffn5+tr98RR8vaxV3268Xqaerk+3XlyRecwLb/vwdfpOSbN3++dczVZ6O/bTk67r90y8dAvs1k+V//fWg9f9i/f2Xbrn947f7937M9i7/zz/+Pv9vv/0vuksz7Q=="))))