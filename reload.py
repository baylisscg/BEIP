#
#
#

import avro
import avro.datafile
import avro.schema
import avro.io

json_schema = '''{
  "namespace": "au.edu.unimelb.eresearch.beip",
  "name":"SensorReading",
  "type":"record",
  "doc":"A simple record for holding a result from a sensor",
  "fields":[{"name":"DateStamp","type":"long"},
            {"name":"Name","type":"string"},
            {"name":"Value","type":"long"}]
}'''

SCHEMA = avro.schema.parse(json_schema)


def main():
    f = None
    try:
        f = open("temp1","r")
        rec_reader = avro.io.DatumReader()
 
        # Create a 'data file' (avro file) reader
        df_reader = avro.datafile.DataFileReader(f, rec_reader)
 
        # Read all records stored inside
        for record in df_reader:
            print "@{0} {1} = {2}\t\t{3}".format( record['DateStamp'], record['Name'], record['Value'],)

    finally:
      if f is not None :
          f.close()

  

if __name__ == '__main__':
  main()
