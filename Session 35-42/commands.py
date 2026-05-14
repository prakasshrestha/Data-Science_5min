show dbs

#create
use newdb
db.user.insert({name: "Shridhar", age: 27})
db.user.insertOne({name: "Manish", age: 40})
db.cars.insertMany( [
      { Car: "c1", wt: 500 },
      { Car: "c2", wt: 600 },
      { Car: "c3" , wt: 900 }
   ])

#Read
db.cars.find()
db.cars.find({wt:500})
db.cars.find({wt:(500,600)})
db.cars.find({wt:(900,600)})
db.cars.find({wt: { $in: [ 600, 900 ] }})
db.cars.find({Car: 'c1',wt: { $lt: 600 }})
db.cars.find({Car: 'c3',wt: { $gt: 600 }})
db.cars.find({Car: 'c2',wt: 600 })
db.cars.find({$or: [{ Car: 'c2' }, { wt: { $lt: 600 }}]})
db.cars.find({$and: [{ Car: 'c1' }, { wt: { $lt: 600 }}]})
db.cars.find({Car: 'c2', $or: [{ wt: { $lt: 900 } }, { wt: { $gt: 900 }  }]})

#Update
db.cars.updateOne({Car:"c1"},{$set:{wt:400}})
                              
db.cars.updateMany({ wt: { $lt: 700 } },
  {
    $set: { Car: 'c0' }
  })

db.cars.replaceOne(
  { Car: 'c3' },
  {
    Car: 'c3', wt:1000
  })

#Delete
db.cars.deleteMany({})
db.bikes.insertOne({_id: ObjectId("563237a41a4d68582c2509da"),name: "BB1",wt: 400,type: "new",limit: 48.90 })
db.bikes.deleteOne( { _id: ObjectId("563237a41a4d68582c2509da") } )       

db.students.insertMany([
  {
    name: 'Shridhar',
    age: 27,
    height: 6
  },
  {
    name: 'Pooja',
    age: 25,
    height: 5.1
  },
  {
    name: 'Manisha',
    age: 40,
    height: 5.2
  }
])
db.students.deleteMany({height: { $lt: 6 }})
db.students.remove( { age: { $gt: 20 } })
db.collection.drop({})

#Sort
db.students.find().sort({name:1})
db.students.find().sort({age:-1})
db.students.aggregate([{ $sort : { age : -1 } }])

#Skip
db.students.find().skip(1)
db.students.find().skip(2)
db.students.aggregate([{ $skip : 1 }])

#Limit
db.students.find().limit(1)
db.students.aggregate([{ $limit : 1 }])
db.students.aggregate([{ $limit : 2 }])
db.students.find().skip(1).limit(1)

#datatype
db.type.insertMany([
    {
       "_id": 1,
       "value": "String"
   },
   {
      "_id": 2,
      "value": 1
   },
   {
      "_id": 3,
      "value": 1.1
   },
   {
      "_id": 4,
      "value": true
   },
   {
      "_id": 5,
      "value": null
   },
   {
      "_id": 6,
      "value": null
   },
   {
      "_id": 7,
      "value": ['a','b','c']
   },
   {
      "_id": 8,
      "value": {name: "Shridhar",
                age: 27}
   },
   {
      "_id": 10,
      "value": 100000.5005005
   },

])
var myDate = Date();
myDate

#ifelse
db.students.insertMany([
  {
    name: 'Shridhar',
    age: 27,
    height: 6
  },
  {
    name: 'Pooja',
    age: 25,
    height: 5.1
  },
  {
    name: 'Manisha',
    age: 40,
    height: 5.2
  }
])
db.students.aggregate([{$project: {height : {$cond: { if: { $gt: [ "$age", 30 ] }, then: 6.5, else: 7 }}}}])
db.students.aggregate([{$project: {height : {$cond: [ { $gte: [ "$age", 30 ] }, 6.5, 7 ]}}}])

#Variable
var x = 5
db.post.insertOne({age: x})
db.type.find( { value: { $type: "object" } } )
db.type.find( { value: { $type: "string" } } )
db.type.find( { value: { $type: "bool" } } )
db.type.find( { value: { $type: "double" } } )
db.type.find( { value: { $type: "int" } } )
db.type.find( { value: { $type: "array" } } )
db.type.find( { value: { $type: "null" } } )

#Index
db.students.createIndex(
  {
      "age": 1
  }
)
db.students.createIndex(
  {
      "height": 1
  }
)
db.students.createIndex({age: 1, height:1})
db.students.getIndexes()
db.students.dropIndex({height:1})
db.students.dropIndexes({age: 1, height : 1})

db.type.find({"_id":7}).pretty()
db.type.find({"value":['a','b','c']}).pretty()

#Embedded Data Model
db.model.insertOne({
    _id: 1 ,
    Std_ID: "1000DF3",
    name:{
        name: "Shridhar"
    },
    address: {
        addr: "ABC Gali"
    },
    phone: {
        phoneno: 9999999999
    }
})

#Normalized Data Model
db.normal.insertOne({_id: 1,
    pid: "1001"})

db.normal.insertOne({  _id: 2,
    pcid: " 1001",
    Name: "Shridhar"})

db.normal.insertOne({  _id: 3,
    pcid: " 1001",
    mail: "abc@gmail.com"})

#Operators
$eq, $ne, $gt, $gte, $lt, $lte, $in, $and, $or, $type

console. clear()
