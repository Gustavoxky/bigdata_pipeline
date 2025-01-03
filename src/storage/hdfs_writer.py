class HDFSWriter:
    def __init__(self, hdfs_path):
        self.hdfs_path = hdfs_path

    def write_to_hdfs(self, df):
        df.write.mode("overwrite").parquet(self.hdfs_path)
