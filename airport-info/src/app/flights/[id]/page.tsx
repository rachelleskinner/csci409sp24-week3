export default function AirportInfo({ params }: { params: { id: string} }){
    return(
        <div>Hello From Flight # {params.id}</div>
    )
}